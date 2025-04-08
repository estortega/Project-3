document.addEventListener('DOMContentLoaded', function () {
    const select = document.getElementById('data-selection');
    const chartContainer = document.getElementById('chart-container');

    select.addEventListener('change', function () {
        const selectedValue = select.value;

        // Clear previous chart
        chartContainer.innerHTML = '';

        // Based on selection, load the corresponding chart
        if (selectedValue === 'chart1') {
            createChart1();
        } else if (selectedValue === 'chart2') {
            createChart2();
        } else if (selectedValue === 'chart3') {
            createChart3();
        }
    });

    function createChart1() {
        // Example code for creating a simple chart (e.g., Bar chart)
        const chart1 = document.createElement('div');
        chart1.innerHTML = '<h2>Chart 1: Alzheimer\'s Statistics</h2><canvas id="chart1Canvas"></canvas>';
        chartContainer.appendChild(chart1);
        const ctx = document.getElementById('chart1Canvas').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Label 1', 'Label 2', 'Label 3'],
                datasets: [{
                    label: 'Dataset 1',
                    data: [10, 20, 30],
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                }]
            }
        });
    }

    function createChart2() {
        // Example for creating another chart (e.g., Line chart)
        const chart2 = document.createElement('div');
        chart2.innerHTML = '<h2>Chart 2: Alzheimer\'s Data Over Time</h2><canvas id="chart2Canvas"></canvas>';
        chartContainer.appendChild(chart2);
        const ctx = document.getElementById('chart2Canvas').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['January', 'February', 'March'],
                datasets: [{
                    label: 'Monthly Data',
                    data: [5, 10, 15],
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            }
        });
    }

    function createChart3() {
        // Example for creating a third type of chart (e.g., Pie chart)
        const chart3 = document.createElement('div');
        chart3.innerHTML = '<h2>Chart 3: Alzheimer\'s Categories</h2><canvas id="chart3Canvas"></canvas>';
        chartContainer.appendChild(chart3);
        const ctx = document.getElementById('chart3Canvas').getContext('2d');
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Category 1', 'Category 2', 'Category 3'],
                datasets: [{
                    label: 'Alzheimer\'s Categories',
                    data: [30, 40, 30],
                    backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)'],
                    borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)'],
                    borderWidth: 1
                }]
            }
        });
    }
});
