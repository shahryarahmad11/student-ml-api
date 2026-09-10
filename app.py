from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Student ML API")

class PredictRequest(BaseModel):
    feature_1: float
    feature_2: float

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "application_version": "1.1.0",
        "model_version": "model-1"
    }

@app.post("/predict")
def predict(data: PredictRequest):
    prediction = (data.feature_1 * 0.5) + (data.feature_2 * 0.5)
    return {
        "prediction": prediction,
        "status": "success"
    }
