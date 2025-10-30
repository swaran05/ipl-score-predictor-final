IPL-Score-Predictor - Final package
This package uses the user's notebook (modified) and includes data, training script, API, and Jenkins pipeline.
Run locally (Windows):
1. python -m venv venv
2. venv\Scripts\activate
3. pip install -r requirements.txt
4. python train_model.py
5. uvicorn app.main:app --reload --port 8000