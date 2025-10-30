from fastapi import FastAPI
from pydantic import BaseModel
import joblib, numpy as np, os

MODEL_PATH = "model.pkl"
app = FastAPI(title="IPL Score Predictor")

class MatchFeatures(BaseModel):
    overs: float
    wickets: int
    runs_so_far: int
    venue_factor: float = 1.0

@app.on_event("startup")
def load_model():
    global model
    try:
        model = joblib.load(MODEL_PATH)
        print("Model loaded from", MODEL_PATH)
    except Exception as e:
        model = None
        print("Model not found:", e)

@app.post("/predict")
def predict(f: MatchFeatures):
    if model is None:
        return {"error":"model not available"}
    X = np.array([[f.overs, f.wickets, f.runs_so_far, f.venue_factor]])
    pred = model.predict(X)
    return {"predicted_score": float(pred[0])}
