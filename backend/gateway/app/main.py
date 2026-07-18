from fastapi import FastAPI
from fastapi.responses import Response
from prometheus_client import Counter, Histogram, generate_latest
from .routes import router

app = FastAPI(
    title="AI Gateway",
    version="1.0.0",
)

app.include_router(router)

REQUEST_COUNT = Counter(
    "gateway_requests_total",
    "Total Gateway Requests"
)

REQUEST_TIME = Histogram(
    "gateway_request_duration_seconds",
    "Gateway Request Duration"
)

@app.get("/")
def root():
    REQUEST_COUNT.inc()
    return {"service": "AI Gateway"}

@app.get("/health")
def health():
    REQUEST_COUNT.inc()
    return {"status": "healthy"}

@app.get("/metrics")
def metrics():
    return Response(
        content=generate_latest(),
        media_type="text/plain"
    )