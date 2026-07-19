---
title: AI Inference Backend
emoji: 🤖
colorFrom: red
colorTo: blue
sdk: docker
pinned: false
license: mit
---

# AI Inference Backend

Combined backend service providing:
- 😊 Sentiment Analysis (DistilBERT)
- 📄 Resume Text Extraction (PyMuPDF)
- 🖼️ Image Classification (Vision Transformer)

## API Endpoints

- `POST /sentiment` - Analyze text sentiment
- `POST /resume` - Extract text from PDF
- `POST /image` - Classify image content
- `GET /health` - Health check

## Usage

This backend is designed to work with the AI Inference Frontend Streamlit app.

### Sentiment Analysis
```bash
curl -X POST https://your-space.hf.space/sentiment \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this product!"}'
```

### Resume Parser
```bash
curl -X POST https://your-space.hf.space/resume \
  -F "file=@resume.pdf"
```

### Image Classification
```bash
curl -X POST https://your-space.hf.space/image \
  -F "file=@image.jpg"
```

## Notes

- First request may take 1-2 minutes (model loading)
- Models are cached after first load
- Free tier may have cold starts
