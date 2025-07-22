import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.metrics import r2_score
import os

# Load the dataset (replace 'forestfires.csv' with the actual dataset)
data = pd.read_csv('data/forestfires.csv')

# Select relevant features and target
X = data[['temp', 'RH', 'wind', 'rain']]  # Features (temperature, humidity, wind speed, rainfall)
y = data['area']  # Target variable (fire area)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define models to try
models = {
    'RandomForest': RandomForestRegressor(n_estimators=100, random_state=42),
    'GradientBoosting': GradientBoostingRegressor(n_estimators=100, random_state=42),
    'LinearRegression': LinearRegression(),
    'SVR': SVR()
}

best_score = float('-inf')
best_model = None
best_model_name = ''

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score = r2_score(y_test, y_pred)
    print(f"{name} R2 score: {score:.4f}")
    if score > best_score:
        best_score = score
        best_model = model
        best_model_name = name

# Save the best model
os.makedirs('model', exist_ok=True)
joblib.dump(best_model, 'model/forest_fire_model.pkl')
print(f"Best model: {best_model_name} with R2 score: {best_score:.4f}")
