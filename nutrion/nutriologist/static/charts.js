var value = JSON.parse(document.getElementById('hello-data').textContent);
console.log(value);
console.log(value.weight)


var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [{
            label: 'Progreso',
            data: value.weight,
            borderColor:['red']
        }],
        labels: value.date.reverse()
    },
    options : {

    }
});
