from fastapi import FastAPI

from .routes import router

app = FastAPI(
    title="Sentiment Service",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "service": "Sentimental Service",
        "status": "running"
    }
    
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

