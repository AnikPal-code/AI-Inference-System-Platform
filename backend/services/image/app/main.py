from fastapi import FastAPI

from .routes import router

app = FastAPI(
    title="Image Service",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "service": "Image Service"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }