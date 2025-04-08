from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

# Load the dataset
df = pd.read_csv("data/cleaned_alzheimers_disease_data.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    # Default values
    gender = request.form.get("gender", "All")
    age_group = request.form.get("age_group", "All")

    # Create age bins
    df["AgeGroup"] = pd.cut(df["Age"], bins=[59, 69, 79, 89, 99], labels=["60–69", "70–79", "80–89", "90+"])

    filtered = df.copy()
    if gender != "All":
        filtered = filtered[filtered["Gender"] == gender]
    if age_group != "All":
        filtered = filtered[filtered["AgeGroup"] == age_group]

    # Create Plotly chart
    chart = px.histogram(filtered, x="Diagnosis", color="Gender", title="Diagnosis Count", barmode="group")
    chart_html = pio.to_html(chart, full_html=False)

    return render_template("index.html", plot=chart_html, gender=gender, age_group=age_group)

if __name__ == "__main__":
    app.run(debug=True)

