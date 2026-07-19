"""
Combined Backend for Hugging Face Spaces
All services (Gateway, Sentiment, Resume, Image) in one FastAPI app
"""

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline
from PIL import Image
import io
import fitz  # PyMuPDF

# Initialize FastAPI app
app = FastAPI(
    title="AI Inference Backend",
    description="Combined backend with Sentiment, Resume, and Image services",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================
# Models Initialization (Lazy Loading)
# ============================================

_sentiment_pipeline = None
_image_classifier = None


def get_sentiment_pipeline():
    """Lazy load sentiment analysis model"""
    global _sentiment_pipeline
    if _sentiment_pipeline is None:
        print("Loading sentiment model...")
        _sentiment_pipeline = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
        print("Sentiment model loaded!")
    return _sentiment_pipeline


def get_image_classifier():
    """Lazy load image classification model"""
    global _image_classifier
    if _image_classifier is None:
        print("Loading image classification model...")
        _image_classifier = pipeline(
            task="image-classification",
            model="google/vit-base-patch16-224"
        )
        print("Image classification model loaded!")
    return _image_classifier


# ============================================
# Schemas
# ============================================

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


# ============================================
# Root & Health Endpoints
# ============================================

@app.get("/")
def root():
    return {
        "service": "AI Inference Backend",
        "status": "running",
        "endpoints": {
            "sentiment": "/sentiment",
            "resume": "/resume",
            "image": "/image",
            "health": "/health"
        }
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


# ============================================
# Sentiment Analysis Service
# ============================================

@app.post("/sentiment", response_model=SentimentResponse)
def sentiment_analysis(request: SentimentRequest):
    """Analyze sentiment of text"""
    try:
        model = get_sentiment_pipeline()
        result = model(request.text)[0]
        
        return SentimentResponse(
            label=result['label'],
            score=result['score']
        )
    except Exception as e:
        print(f"Sentiment analysis error: {e}")
        return SentimentResponse(
            label="ERROR",
            score=0.0
        )


# ============================================
# Resume Parser Service
# ============================================

@app.post("/resume", response_model=ResumeResponse)
async def resume_parser(file: UploadFile = File(...)):
    """Extract text from PDF resume"""
    try:
        # Read PDF bytes
        pdf_bytes = await file.read()
        
        # Extract text using PyMuPDF
        text = ""
        with fitz.open(stream=pdf_bytes, filetype="pdf") as document:
            for page in document:
                text += page.get_text()
        
        return ResumeResponse(
            extracted_text=text if text.strip() else "No text could be extracted from the PDF."
        )
    except Exception as e:
        print(f"Resume parsing error: {e}")
        return ResumeResponse(
            extracted_text=f"Error extracting text: {str(e)}"
        )


# ============================================
# Image Classification Service
# ============================================

@app.post("/image", response_model=ImageResponse)
async def image_classification(file: UploadFile = File(...)):
    """Classify image content"""
    try:
        # Read image bytes
        image_bytes = await file.read()
        
        # Open image with PIL
        image = Image.open(io.BytesIO(image_bytes))
        
        # Classify image
        classifier = get_image_classifier()
        result = classifier(image)[0]
        
        return ImageResponse(
            label=result['label'],
            score=result['score']
        )
    except Exception as e:
        print(f"Image classification error: {e}")
        return ImageResponse(
            label="ERROR",
            score=0.0
        )


# ============================================
# Startup Event
# ============================================

@app.on_event("startup")
async def startup_event():
    """Pre-load models on startup (optional)"""
    print("=" * 50)
    print("AI Inference Backend Starting...")
    print("=" * 50)
    print("Models will be loaded on first request")
    print("This is normal and may take 1-2 minutes")
    print("=" * 50)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
