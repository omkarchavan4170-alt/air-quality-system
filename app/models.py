from pydantic import BaseModel

class AQData(BaseModel):
    pm25: float
    pm10: float
    no2: float
    co: float
