import os
import asyncio
import httpx

SENTIMENT_URL = os.getenv("SENTIMENT_URL")
RESUME_URL = os.getenv("RESUME_URL")
IMAGE_URL = os.getenv("IMAGE_URL")


async def post_json(service_url: str, endpoint: str, payload: dict):
    url = f"{service_url}{endpoint}"

    async with httpx.AsyncClient(timeout=60.0) as client:
        for _ in range(10):
            try:
                response = await client.post(url, json=payload)
                response.raise_for_status()
                return response.json()
            except httpx.ConnectError:
                await asyncio.sleep(2)

    raise RuntimeError(f"Cannot connect to {url}")


async def post_file(service_url: str, endpoint: str, files: dict):
    url = f"{service_url}{endpoint}"

    async with httpx.AsyncClient(timeout=60.0) as client:
        for _ in range(10):
            try:
                response = await client.post(url, files=files)
                response.raise_for_status()
                return response.json()
            except httpx.ConnectError:
                await asyncio.sleep(2)

    raise RuntimeError(f"Cannot connect to {url}")