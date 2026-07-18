# Schemas defines the shape/structure of the data
# that our API expects to recieve or send.
# Like a contract between client and API

from pydantic import BaseModel


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    label: str
    score: float