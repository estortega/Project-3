from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('data/cleaned_alzheimers_disease_data.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart-data/<chart_id>')
def chart_data(chart_id):
    if chart_id == 'chart1':
        data = df['Gender'].value_counts()
        return jsonify({
            'title': "Gender Distribution",
            'type': 'bar',
            'labels': list(data.index),
            'data': list(data.values),
            'datasetLabel': 'Number of Patients',
            'backgroundColor': ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)'],
            'borderColor': ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)']
        })
    elif chart_id == 'chart2':
        data = df['Age'].value_counts().sort_index()
        return jsonify({
            'title': "Age Distribution",
            'type': 'line',
            'labels': list(map(str, data.index)),
            'data': list(data.values),
            'datasetLabel': 'Patient Count by Age',
            'backgroundColor': ['rgba(75, 192, 192, 0.2)'],
            'borderColor': ['rgba(75, 192, 192, 1)']
        })
    elif chart_id == 'chart3':
        data = df['Diagnosis'].value_counts()
        return jsonify({
            'title': "Diagnosis Breakdown",
            'type': 'pie',
            'labels': list(data.index),
            'data': list(data.values),
            'datasetLabel': 'Diagnosis Distribution',
            'backgroundColor': ['rgba(255, 206, 86, 0.2)', 'rgba(153, 102, 255, 0.2)'],
            'borderColor': ['rgba(255, 206, 86, 1)', 'rgba(153, 102, 255, 1)']
        })
    else:
        return jsonify({'error': 'Invalid chart ID'}), 400