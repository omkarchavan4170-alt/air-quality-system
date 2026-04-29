import joblib
import numpy as np

model = joblib.load("ml/model.pkl")

def predict(data):
    features = np.array([[data["pm25"], data["pm10"], data["no2"], data["co"]]])
    return float(model.predict(features)[0])