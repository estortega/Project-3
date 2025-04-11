document.addEventListener('DOMContentLoaded', function () {
    const select = document.getElementById('data-selection');
    const chartContainer = document.getElementById('chart-container');

    select.addEventListener('change', function () {
        const selectedValue = select.value;

        // Clear previous chart
        chartContainer.innerHTML = '';

        // Load chart data from Flask backend
        fetch(`/chart-data/${selectedValue}`)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                renderChart(selectedValue, data);
            })
            .catch(error => {
                console.error('Error fetching chart data:', error);
            });
    });

    function renderChart(chartId, chartData) {
        const chartWrapper = document.createElement('div');
        chartWrapper.innerHTML = `<h2>${chartData.title}</h2><canvas id="${chartId}Canvas"></canvas>`;
        chartContainer.appendChild(chartWrapper);

        const ctx = document.getElementById(`${chartId}Canvas`).getContext('2d');
        new Chart(ctx, {
            type: chartData.type,
            data: {
                labels: chartData.labels,
                datasets: [{
                    label: chartData.datasetLabel,
                    data: chartData.data,
                    backgroundColor: chartData.backgroundColor,
                    borderColor: chartData.borderColor,
                    borderWidth: 1
                }]
            }
        });
    }
});
