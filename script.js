function fetchData() {
    fetch('http://127.0.0.1:5000/azkar')
        .then(response => response.json())
        .then(data => {
            const output = document.getElementById('azkar-output');
            output.innerHTML = data.map(dhikr => <p>${dhikr}</p>).join('');
        })
        .catch(err => console.error(err));
}

function fetchWudu() {
    fetch('http://127.0.0.1:5000/wudu')
        .then(response => response.json())
        .then(data => {
            const output = document.getElementById('wudu-output');
            output.innerHTML = data.map(step => <p>${step}</p>).join('');
        })
        .catch(err => console.error(err));
}