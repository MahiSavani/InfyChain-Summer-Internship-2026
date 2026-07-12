#!/usr/bin/env python3
"""
FastAPI backend for Kyphosis prediction web application.

This API provides endpoints for health checks and kyphosis prediction
using a pre-trained Decision Tree model.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
import joblib
import numpy as np
import os
from typing import Dict, Any

# Initialize FastAPI app
app = FastAPI(
    title="Kyphosis Prediction API",
    description="A simple API to predict spinal kyphosis based on patient data",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Global variable to store the loaded model
model = None

# Pydantic models for request/response validation
class PredictionRequest(BaseModel):
    age: int = Field(..., description="Patient age in months", gt=0, le=250)
    number: int = Field(..., description="Number of vertebrae involved", gt=0, le=20)
    start: int = Field(..., description="Topmost vertebra level operated on", gt=0, le=20)
    
    @validator('age')
    def validate_age(cls, v):
        if v <= 0 or v > 250:
            raise ValueError('Age must be between 1 and 250 months')
        return v
    
    @validator('number')
    def validate_number(cls, v):
        if v <= 0 or v > 20:
            raise ValueError('Number of vertebrae must be between 1 and 20')
        return v
    
    @validator('start')
    def validate_start(cls, v):
        if v <= 0 or v > 20:
            raise ValueError('Start vertebra level must be between 1 and 20')
        return v

class PredictionResponse(BaseModel):
    prediction: str = Field(..., description="Prediction result: 'present' or 'absent'")
    confidence: float = Field(..., description="Confidence score between 0 and 1")

class HealthResponse(BaseModel):
    status: str
    message: str

class MetricsResponse(BaseModel):
    accuracy: float
    precision: float
    recall: float
    f1_score: float

def load_model():
    """Load the pre-trained model from disk."""
    global model
    model_path = "model.pkl"
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Model file '{model_path}' not found. Please run train_model.py first."
        )
    
    try:
        model = joblib.load(model_path)
        print(f"Model loaded successfully from {model_path}")
    except Exception as e:
        raise RuntimeError(f"Failed to load model: {e}")

# Load model on startup
@app.on_event("startup")
async def startup_event():
    """Initialize the application on startup."""
    try:
        load_model()
        print("FastAPI server started successfully!")
    except Exception as e:
        print(f"Error during startup: {e}")
        raise

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint to verify the API is running.
    
    Returns:
        Dict with status and message
    """
    return HealthResponse(
        status="ok",
        message="Kyphosis Prediction API is running"
    )

@app.post("/predict", response_model=PredictionResponse)
async def predict_kyphosis(request: PredictionRequest):
    """
    Predict kyphosis based on patient data.
    
    Args:
        request: PredictionRequest with age, number, and start values
        
    Returns:
        PredictionResponse with prediction and confidence
        
    Raises:
        HTTPException: If model is not loaded or prediction fails
    """
    if model is None:
        raise HTTPException(
            status_code=500,
            detail="Model not loaded. Please check server logs."
        )
    
    try:
        # Prepare input data
        input_data = np.array([[request.age, request.number, request.start]])
        
        # Make prediction
        prediction_proba = model.predict_proba(input_data)[0]
        prediction_class = model.predict(input_data)[0]
        
        # Convert prediction to string
        prediction_str = "present" if prediction_class == 1 else "absent"
        
        # Calculate confidence (probability of predicted class)
        confidence = float(max(prediction_proba))
        
        return PredictionResponse(
            prediction=prediction_str,
            confidence=confidence
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )

@app.get("/metrics", response_model=MetricsResponse)
async def get_model_metrics():
    """
    Get model performance metrics.
    
    Returns:
        MetricsResponse with accuracy, precision, recall, and F1-score
    """
    # These are the metrics from our trained model (from the training output)
    return MetricsResponse(
        accuracy=0.7750,
        precision=0.50,
        recall=0.40,
        f1_score=0.44
    )

@app.get("/")
async def root():
    """
    Root endpoint with basic API information.
    
    Returns:
        Dict with API information
    """
    return {
        "message": "Kyphosis Prediction API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "predict": "/predict",
            "docs": "/docs"
        },
        "description": "Submit patient data to /predict endpoint to get kyphosis prediction"
    }

if __name__ == "__main__":
    import uvicorn
    import multiprocessing
    
    # Required for Windows compatibility with multiprocessing
    multiprocessing.freeze_support()
    
    uvicorn.run(app, host="0.0.0.0", port=8000)