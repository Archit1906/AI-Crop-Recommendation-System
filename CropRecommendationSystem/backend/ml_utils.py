import joblib
import os
import pandas as pd
from typing import Tuple

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_dir = os.path.join(base_dir, 'model')

# Global variables to hold loaded artifacts
model = None
scaler = None
encoder = None

def load_artifacts():
    global model, scaler, encoder
    try:
        model = joblib.load(os.path.join(model_dir, 'model.pkl'))
        scaler = joblib.load(os.path.join(model_dir, 'scaler.pkl'))
        encoder = joblib.load(os.path.join(model_dir, 'encoder.pkl'))
        print("ML artifacts loaded successfully.")
    except Exception as e:
        print(f"Error loading ML artifacts: {e}. Has the model been trained?")

def predict_crop(N: float, P: float, K: float, temperature: float, humidity: float, ph: float, rainfall: float) -> Tuple[str, float]:
    if model is None or scaler is None or encoder is None:
        raise ValueError("Model artifacts are not loaded.")

    # Prepare input data matching the training format
    features = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]], 
                            columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    
    # Scale features
    features_scaled = scaler.transform(features)

    # Predict
    pred_encoded = model.predict(features_scaled)
    crop_name = encoder.inverse_transform(pred_encoded)[0]

    # Confidence score
    probabilities = model.predict_proba(features_scaled)[0]
    confidence_score = max(probabilities)

    return crop_name, confidence_score
