function datum(dana=0) {
    if(dana===0){
        var today = new Date();
    } else {
        var today = new Date();
        today.setDate(today.getDate()- this.dana);
    }
    var dd = today.getDate();
    var mm = today.getMonth()+1;
    var yyyy = today.getFullYear();
    if(dd<10)
    {
        dd='0'+dd;
    }

    if(mm<10)
    {
        mm='0'+mm;
    }
    return dd+'.'+mm+'.'+yyyy
}

today = datum(dana=0)
before_today = datum(dana=30)
url = 'http://127.0.0.1:5000/api/v1/pelud?grad=Zagreb&datum='+before_today+'|'+today

function uniq(a) {
    return Array.from(new Set(a));
}

var request = new XMLHttpRequest()

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', url, true)

request.onload = function () {
    // Begin accessing JSON data here
    var data = JSON.parse(this.responseText);
    var datasets = {}
    datas = []
    labels = []
    for (d in data) {
        labels.push(data[d]['Zagreb']['datum']);
        if (data[d]['Zagreb']['biljka'] in datasets){
            datasets[data[d]['Zagreb']['biljka']]['data'].push(data[d]['Zagreb']['vrijednost']);

        } else {
            var one = Math.random()*256|0
            var two = Math.random()*256|0
            var three = Math.random()*256|0
            var rgba = 'rgba('+ one +',' + two + ',' + three + ')'
            vrijednost = []
            datasets[data[d]['Zagreb']['biljka']] = {label: data[d]['Zagreb']['biljka'],
                                                     data: [data[d]['Zagreb']['vrijednost']],
                                                     fill: false,
                                                     backgroundColor: [rgba],
                                                     borderColor: [rgba],
                                                     pointStyle: 'rectRot',}
        };

    }
    for (d in datasets){
        myChart.data.datasets.push(datasets[d])

    }
    labels = uniq(labels)
    myChart.data.labels = labels
}

// Send request
request.send()

var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {},
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: false
                }
            }]
        }
    }
});