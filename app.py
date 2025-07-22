
from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np
import json

app = Flask(__name__)

# Load the trained RandomForest model
model = joblib.load('model/forest_fire_model.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/monitoring')
def monitoring():
    return render_template('fire_monitoring.html')


@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/tips')
def tips():
    return render_template('tips.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Prediction page route
@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        # Retrieve the input data from the form
        temp = float(request.form['temp'])
        humidity = float(request.form['humidity'])
        wind = float(request.form['wind'])
        rain = float(request.form['rain'])

        # Prepare the input features for prediction
        features = np.array([[temp, humidity, wind, rain]])

        # Make the prediction using the trained model
        predicted_area = model.predict(features)[0]

        # Determine fire risk based on predicted area
        fire_risk = "High" if predicted_area > 10 else "Low"
        probability = round(predicted_area / 100, 2)  # Convert to a probability scale

        return render_template('prediction.html', fire_risk=fire_risk, probability=probability)

    return render_template('prediction.html')


# Sample in-memory data for fire alerts (this could be replaced with a database or file storage)
alerts_data = [
    {"region": "California", "severity": "High", "notification": "SMS"},
    {"region": "Nevada", "severity": "Low", "notification": "Email"}
]

# Route for Fire Alerts Page
@app.route('/alerts', methods=['GET', 'POST'])
def fire_alerts():
    if request.method == 'POST':
        region = request.form['region']
        severity = request.form['severity']
        notification = request.form['notification']
        # Add new alert to the alerts_data (this would be saved in a database in a real app)
        alerts_data.append({"region": region, "severity": severity, "notification": notification})
        # Redirect back to the alerts page to see the updated list
        return redirect(url_for('fire_alerts'))
    return render_template('alerts.html', alerts=alerts_data)

if __name__ == '__main__':
    app.run(debug=True)


