def predict_aqi(data):
    aqi = (
        0.4 * data["pm25"] +
        0.3 * data["pm10"] +
        0.2 * data["no2"] +
        0.1 * data["co"]
    )
    return round(aqi, 2)