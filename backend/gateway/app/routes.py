from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel

from .client import (
    post_json,
    post_file,
    SENTIMENT_URL,
    RESUME_URL,
    IMAGE_URL,
)

router = APIRouter()


class TextRequest(BaseModel):
    text: str


@router.post("/sentiment")
async def sentiment(request: TextRequest):
    return await post_json(
        SENTIMENT_URL,
        "/predict",
        request.model_dump(),
    )


@router.post("/resume")
async def resume(file: UploadFile = File(...)):
    files = {
        "file": (
            file.filename,
            await file.read(),
            file.content_type,
        )
    }

    return await post_file(
        RESUME_URL,
        "/extract",
        files,
    )


@router.post("/image")
async def image(file: UploadFile = File(...)):
    files = {
        "file": (
            file.filename,
            await file.read(),
            file.content_type,
        )
    }

    return await post_file(
        IMAGE_URL,
        "/predict",
        files,
    )