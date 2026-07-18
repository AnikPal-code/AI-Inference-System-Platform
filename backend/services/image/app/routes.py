from fastapi import APIRouter, File, UploadFile
from PIL import Image
import io

from .model import classify_image
from .schemas import ImageResponse

router = APIRouter()


@router.post("/predict", response_model=ImageResponse)
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()

    image = Image.open(io.BytesIO(image_bytes))

    prediction = classify_image(image)

    return ImageResponse(
        label=prediction["label"],
        score=prediction["score"]
    )