from app.database import SessionLocal
from app.database import Base
from sqlalchemy import Column, Float, Integer

class AQDataDB(Base):
    __tablename__ = "aq_data"

    id = Column(Integer, primary_key=True, index=True)
    pm25 = Column(Float)
    pm10 = Column(Float)
    no2 = Column(Float)
    co = Column(Float)

Base.metadata.create_all(bind=SessionLocal().bind)

def save_data(data):
    db = SessionLocal()
    record = AQDataDB(**data)
    db.add(record)
    db.commit()
    db.close()

def get_latest():
    db = SessionLocal()
    data = db.query(AQDataDB).order_by(AQDataDB.id.desc()).first()
    db.close()
    return data