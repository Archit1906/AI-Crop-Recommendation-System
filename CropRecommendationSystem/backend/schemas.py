from pydantic import BaseModel, Field
from typing import Optional

class PredictionRequest(BaseModel):
    N: float = Field(..., description="Nitrogen content in soil")
    P: float = Field(..., description="Phosphorus content in soil")
    K: float = Field(..., description="Potassium content in soil")
    temperature: Optional[float] = Field(None, description="Temperature in Celsius")
    humidity: Optional[float] = Field(None, description="Humidity percentage")
    ph: float = Field(..., description="pH value of the soil")
    rainfall: float = Field(..., description="Rainfall in mm")
    city: Optional[str] = Field(None, description="City name to fetch real-time weather")

class PredictionResponse(BaseModel):
    crop: str
    confidence: str
    tips: dict
