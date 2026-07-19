# Streamlit Frontend

This is the Streamlit-based frontend for the AI Inference Platform.

## Configuration

1. Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

2. Update the `.env` file with your configuration:
```env
GATEWAY_URL=http://localhost:8000
```

## Running the App

```bash
streamlit run app.py
```

The app will be available at http://localhost:8501

## Environment Variables

- `GATEWAY_URL`: The URL of the API Gateway (default: http://localhost:8000)

## Pages

- **Home** (`app.py`): Landing page with service overview
- **Sentiment Analysis** (`pages/sentiment.py`): Analyze text sentiment
- **Resume Parser** (`pages/resume.py`): Extract text from PDF resumes
- **Image Classification** (`pages/image.py`): Classify images using AI
