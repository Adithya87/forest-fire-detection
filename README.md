
# Forest Fire Detection Web Application

A modern web application for real-time forest fire risk prediction, monitoring, and community alerts. Built with Flask, scikit-learn, and a responsive frontend.

## Features
- **Real-Time Fire Monitoring:** Interactive map with live fire data visualization.
- **AI-Powered Prediction:** Predicts forest fire probability using environmental data and a trained machine learning model.
- **Community Alerts:** Users can set up custom alerts for specific regions and receive notifications.
- **Reports & Analytics:** Visualize fire trends and analytics with charts.
- **Prevention Tips:** Educational resources to help prevent forest fires.

## Technologies Used
- Python, Flask
- scikit-learn, joblib, numpy
- HTML5, CSS3, JavaScript
- Chart.js, Leaflet.js

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Adithya87/forest-fire-detection.git
   cd forest-fire-detection
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python app.py
   ```
4. Open your browser and go to `http://127.0.0.1:5000/`

### Project Structure
```
app.py
config.py
model/
    forest_fire_model.pkl
    trained_model.py
data/
    forestfires.csv
templates/
    *.html
static/
    style.css
    scripts.js
```

## Usage
- **Home:** Overview and quick access to features.
- **Prediction:** Enter temperature, humidity, wind, and rain to predict fire risk.
- **Monitoring:** View real-time fire locations on a map.
- **Alerts:** Set and view custom fire alerts.
- **Reports:** Analyze fire trends with interactive charts.
- **Tips:** Learn how to prevent forest fires.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [Leaflet.js](https://leafletjs.com/)
- [Chart.js](https://www.chartjs.org/)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/forest+fires)
