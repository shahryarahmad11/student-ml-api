from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="student-ml-api", version="1.0.0")

class PredictRequest(BaseModel):
    value: float | int

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "version": "1.0.0"
    }

@app.post("/predict")
def predict(payload: PredictRequest):
    if payload.value is None:
        raise HTTPException(status_code=400, detail="Missing input")
    
    return {
        "input": payload.value,
        "prediction": payload.value * 2
    }
