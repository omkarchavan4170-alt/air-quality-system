import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = pd.DataFrame({
    "pm25": [10, 20, 30, 40],
    "pm10": [20, 30, 40, 50],
    "no2": [5, 10, 15, 20],
    "co": [1, 2, 3, 4],
    "aqi": [50, 80, 110, 150]
})

X = data[["pm25", "pm10", "no2", "co"]]
y = data["aqi"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "ml/model.pkl")