# AI-Inference-System-Platform

A microservices-based AI platform built with FastAPI, Docker, and Streamlit, offering sentiment analysis, resume parsing, and image classification services.

## 🏗️ Architecture

```
Streamlit UI (Port 3000)
      │
      ▼
FastAPI Gateway (Port 8000)
      │
 ┌────┼────┐
 │    │    │
 ▼    ▼    ▼
Sentiment Resume Image
(8001)   (8002)  (8003)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Docker & Docker Compose (for containerized deployment)
- Virtual environment (recommended)

### Option 1: Run with Docker (Recommended)

1. **Build and start all services:**
```bash
docker-compose up --build
```

2. **Start Streamlit (in a separate terminal):**
```bash
streamlit run streamlit_app/app.py
```

3. **Access the application:**
   - Streamlit UI: http://localhost:8501
   - Gateway API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Option 2: Run Locally (Development)

1. **Create virtual environment:**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Start Gateway:**
```bash
uvicorn backend.gateway.app.main:app --host 0.0.0.0 --port 8000
```

4. **Start Sentiment Service (new terminal):**
```bash
uvicorn backend.services.sentiment.app.main:app --host 0.0.0.0 --port 8001
```

5. **Start Resume Service (new terminal):**
```bash
uvicorn backend.services.resume.app.main:app --host 0.0.0.0 --port 8002
```

6. **Start Image Service (new terminal):**
```bash
uvicorn backend.services.image.app.main:app --host 0.0.0.0 --port 8003
```

7. **Start Streamlit UI (new terminal):**
```bash
streamlit run streamlit_app/app.py
```

## 📦 Services

### 1. Sentiment Analysis Service
- **Endpoint:** `POST /sentiment`
- **Model:** DistilBERT (SST-2)
- **Input:** JSON with `text` field
- **Output:** `label` (POSITIVE/NEGATIVE) and `score` (confidence)

### 2. Resume Parser Service
- **Endpoint:** `POST /resume`
- **Input:** PDF file upload
- **Output:** Extracted text from resume

### 3. Image Classification Service
- **Endpoint:** `POST /image`
- **Model:** Vision Transformer (ViT)
- **Input:** Image file (jpg, png)
- **Output:** `label` (object class) and `score` (confidence)

## 🔧 Configuration

### Backend Services

Environment variables are stored in `backend/.env`:
```env
SENTIMENT_URL=http://localhost:8001
RESUME_URL=http://localhost:8002
IMAGE_URL=http://localhost:8003
```

For Docker deployment, these are automatically configured in `docker-compose.yml`.

### Streamlit Frontend

Create `streamlit_app/.env` file:
```env
GATEWAY_URL=http://localhost:8000
```

Or copy from the example:
```bash
cd streamlit_app
cp .env.example .env
```

## 📊 Monitoring

Gateway includes Prometheus metrics:
- **Metrics Endpoint:** http://localhost:8000/metrics
- **Health Check:** http://localhost:8000/health

## 🛠️ Tech Stack

- **Backend:** FastAPI, Uvicorn
- **ML Models:** Transformers (Hugging Face), PyTorch
- **Frontend:** Streamlit
- **Containerization:** Docker, Docker Compose
- **Monitoring:** Prometheus
- **PDF Processing:** PyMuPDF (fitz)
- **Image Processing:** PIL, torchvision

## 📝 API Documentation

Once the gateway is running, interactive API documentation is available at:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 🐛 Troubleshooting

### Connection Errors
- Ensure all services are running
- Check if ports 8000-8003 are available
- Verify `.env` file exists in `backend/` directory

### Docker Issues
- Run `docker-compose down` and `docker-compose up --build` to rebuild
- Check logs: `docker-compose logs <service-name>`

### Model Download Delays
- First run downloads models from Hugging Face (may take a few minutes)
- Models are cached for subsequent runs

## 📄 License

This project is for educational and demonstration purposes.