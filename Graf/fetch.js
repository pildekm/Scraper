
var today = new Date();
today.setHours(0, 0, 0, 0);
console.log(today)
url = 'http://127.0.0.1:5000/api/v1/pelud?grad=Zagreb&datum=13.02.2020'
fetch(url)
    .then(function (res) {
        var data = res.json();
        console.log(data)
        return data
    })