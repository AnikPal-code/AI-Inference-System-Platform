from pydantic import BaseModel


class ImageResponse(BaseModel):
    label: str
    score: float