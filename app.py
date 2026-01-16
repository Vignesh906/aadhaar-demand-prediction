
from flask import Flask, render_template
import pandas as pd
from forecast import forecast_demand
from anomaly import detect_anomaly
from mobile_plan import mobile_van_plan

app = Flask(__name__)

@app.route("/")
def home():
    return "UIDAI Aadhaar Demand Prediction AI System Running"

@app.route("/forecast/<district>")
def forecast(district):
    return forecast_demand(district)

@app.route("/anomaly")
def anomaly():
    return detect_anomaly()

@app.route("/mobile")
def mobile():
    return mobile_van_plan()

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

