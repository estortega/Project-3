from flask import Flask, render_template, jsonify
import json
from collections import defaultdict
import os

app = Flask(__name__, static_folder='statics', template_folder='templates')

# Load the dataset
with open('statics/cleaned_alzheimers_disease_data.json') as f:
    data = json.load(f)

def get_age_range(age):
    if age < 65:
        return '<65'
    elif age < 70:
        return '65-69'
    elif age < 75:
        return '70-74'
    elif age < 80:
        return '75-79'
    elif age < 85:
        return '80-84'
    else:
        return '85+'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/ethnicity')
def ethnicity_data():
    grouped = defaultdict(lambda: defaultdict(int))
    for entry in data:
        age = entry.get('Age')
        ethnicity = entry.get('Ethnicity') or 'Unknown'
        if age:
            age_range = get_age_range(age)
            grouped[age_range][ethnicity] += 1

    response = {
        'labels': sorted(grouped.keys()),
        'categories': list({eth for val in grouped.values() for eth in val}),
        'data': grouped
    }
    return jsonify(response)

@app.route('/data/gender')
def gender_data():
    grouped = defaultdict(lambda: defaultdict(int))
    for entry in data:
        age = entry.get('Age')
        gender = entry.get('Gender') or 'Unknown'
        if age:
            age_range = get_age_range(age)
            grouped[age_range][gender] += 1

    response = {
        'labels': sorted(grouped.keys()),
        'categories': list({gen for val in grouped.values() for gen in val}),
        'data': grouped
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
