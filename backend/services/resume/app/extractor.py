# Converts PDF to Plain Text for extraction.

import fitz


def extract_text(pdf_bytes: bytes) -> str:
    """
    Extract text from a PDF using PyMuPDF.
    """

    text = ""

    with fitz.open(stream=pdf_bytes, filetype="pdf") as document:
        for page in document:
            text += page.get_text()

    return text