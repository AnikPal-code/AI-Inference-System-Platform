"""
Vercel Serverless Function - Combined Backend
All services in one endpoint for Vercel deployment
"""

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mangum import Mangum
import io

# Lazy imports to reduce cold start time
app = FastAPI(title="AI Inference Backend")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schemas
class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    score: float

class ImageResponse(BaseModel):
    label: str
    score: float

class ResumeResponse(BaseModel):
    extracted_text: str

# Global model variables
_sentiment_model = None
_image_model = None

def get_sentiment_model():
    global _sentiment_model
    if _sentiment_model is None:
        from transformers import pipeline
        _sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    return _sentiment_model

def get_image_model():
    global _image_model
    if _image_model is None:
        from transformers import pipeline
        _image_model = pipeline("image-classification", model="google/vit-base-patch16-224")
    return _image_model

@app.get("/")
def root():
    return {
        "service": "AI Inference Backend",
        "status": "running",
        "platform": "Vercel"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/sentiment", response_model=SentimentResponse)
def sentiment(request: SentimentRequest):
    try:
        model = get_sentiment_model()
        result = model(request.text)[0]
        return SentimentResponse(label=result['label'], score=result['score'])
    except Exception as e:
        return SentimentResponse(label="ERROR", score=0.0)

@app.post("/resume", response_model=ResumeResponse)
async def resume(file: UploadFile = File(...)):
    try:
        import fitz
        pdf_bytes = await file.read()
        text = ""
        with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return ResumeResponse(extracted_text=text if text.strip() else "No text extracted")
    except Exception as e:
        return ResumeResponse(extracted_text=f"Error: {str(e)}")

@app.post("/image", response_model=ImageResponse)
async def image(file: UploadFile = File(...)):
    try:
        from PIL import Image
        image_bytes = await file.read()
        img = Image.open(io.BytesIO(image_bytes))
        model = get_image_model()
        result = model(img)[0]
        return ImageResponse(label=result['label'], score=result['score'])
    except Exception as e:
        return ImageResponse(label="ERROR", score=0.0)

# Vercel handler
handler = Mangum(app)
