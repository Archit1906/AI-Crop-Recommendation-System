import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
import traceback

# Import from backend modules
from backend.schemas import PredictionRequest, PredictionResponse
from backend.ml_utils import load_artifacts, predict_crop
from backend.external_apis import get_weather

import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from utils.farming_tips import get_tips

app = FastAPI(title="AI Crop Recommendation API", 
              description="API for recommending the best crop based on soil and weather conditions.",
              version="1.0.0")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load machine learning artifacts gracefully at startup
@app.on_event("startup")
def startup_event():
    load_artifacts()

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Crop Recommendation API"}

@app.post("/predict", response_model=PredictionResponse)
def predict(req: PredictionRequest):
    try:
        temp = req.temperature
        hum = req.humidity
        
        # If city is provided and metrics are missing, fetch from Weather API
        if req.city and (temp is None or hum is None):
            weather_data = get_weather(req.city)
            if "error" in weather_data:
                raise HTTPException(status_code=400, detail=f"Weather API Error: {weather_data['error']}. Please provide temperature and humidity manually.")
            
            temp = weather_data.get("temperature", temp)
            hum = weather_data.get("humidity", hum)

        # Fallback if still None
        if temp is None or hum is None:
            raise HTTPException(status_code=400, detail="Temperature and Humidity are required if city is not provided or weather fetch fails.")

        # ML Inference
        crop_name, confidence = predict_crop(
            N=req.N, 
            P=req.P, 
            K=req.K, 
            temperature=temp, 
            humidity=hum, 
            ph=req.ph, 
            rainfall=req.rainfall
        )
        
        tips = get_tips(crop_name)
        
        return PredictionResponse(
            crop=crop_name.capitalize(),
            confidence=f"{confidence * 100:.2f}%",
            tips=tips
        )

    except HTTPException:
        raise
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# To run locally: uvicorn backend.main:app --reload
