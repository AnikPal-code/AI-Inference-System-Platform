# This code creates the core ML engine for the app.
# It loads the AI model via transformers and exposes
# a single function to analyze the emotional tone
from transformers import pipeline

_sentiment_pipeline = None


def get_pipeline():
    global _sentiment_pipeline

    if _sentiment_pipeline is None:
        _sentiment_pipeline = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    return _sentiment_pipeline


def predict_sentiment(text: str):
    model = get_pipeline()
    return model(text)[0]