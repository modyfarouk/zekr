from flask import Flask, jsonify, request
from flask import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///azkar.db'
db = SQLAlchemy(app)

# تعريف جدول للأذكار
class Azkar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), unique=True, nullable=False)

# تعريف جدول لخطوات الوضوء
class WuduSteps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    step = db.Column(db.String(255), unique=True, nullable=False)

# ... (إضافة بيانات إلى الجداول عند تشغيل التطبيق لأول مرة)

@app.route('/azkar', methods=['GET'])
def get_azkar():
    azkar = Azkar.query.all()
    return jsonify([azkar.text for azkar in azkar])

@app.route('/wudu', methods=['GET'])
def get_wudu():
    wudu_steps = WuduSteps.query.all()
    return jsonify([step.step for step in wudu_steps])

if __name__ == '_main_':
    db.create_all()
    app.run(debug=True)