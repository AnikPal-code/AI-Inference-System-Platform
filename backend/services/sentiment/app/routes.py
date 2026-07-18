
# This code defines a single, reusable API 
# endpoint (or route) using the FastAPI framework
# to handle incoming machine learning predictions.
# It takes a piece of text sent by a user, passes it to a sentiment 
# analysis model, and returns whether that text is positive or 
# negative along with a confidence score.


from fastapi import APIRouter
from .model import predict_sentiment
from .schemas import SentimentRequest, SentimentResponse

router = APIRouter()

@router.post("/predict", response_model=SentimentResponse)
def predict(request: SentimentRequest):
    result = predict_sentiment(request.text)
    
    return SentimentResponse(
        label=result['label'],
        score=result['score']
    )
    
