from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict_aqi
from app.utils import data_store

app = FastAPI()

class AQData(BaseModel):
    pm25: float
    pm10: float
    no2: float
    co: float

@app.get("/")
def home():
    return {"message": "Air Quality API Running"}

@app.post("/add-data")
def add_data(data: AQData):
    data_store.append(data.dict())
    return {"status": "Data added", "data": data}

@app.get("/latest")
def get_latest():
    if not data_store:
        return {"error": "No data"}
    return data_store[-1]

@app.post("/predict")
def predict(data: AQData):
    prediction = predict_aqi(data.dict())
    return {"predicted_aqi": prediction}