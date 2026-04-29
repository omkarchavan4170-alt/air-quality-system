from fastapi import FastAPI
from app.models import AQData
from app.crud import save_data, get_latest
from app.ml_model import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Air Quality API Running"}

@app.post("/add-data")
def add_data(data: AQData):
    save_data(data.dict())
    return {"status": "saved"}

@app.get("/latest")
def latest():
    data = get_latest()
    if not data:
        return {"error": "no data"}
    return data.__dict__

@app.post("/predict")
def predict_api(data: AQData):
    result = predict(data.dict())
    return {"aqi": result}