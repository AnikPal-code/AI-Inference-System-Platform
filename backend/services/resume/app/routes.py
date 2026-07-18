from fastapi import APIRouter, File, UploadFile

from .extractor import extract_text
from .schemas import ResumeResponse

router = APIRouter()


@router.post("/extract", response_model=ResumeResponse)
async def extract_resume(file: UploadFile = File(...)):
    pdf_bytes = await file.read()

    text = extract_text(pdf_bytes)

    return ResumeResponse(
        extracted_text=text
    )