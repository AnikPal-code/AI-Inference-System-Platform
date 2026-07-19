import os
import asyncio
from pathlib import Path

import httpx
from dotenv import load_dotenv

# Load .env
dotenv_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path)

SENTIMENT_URL = os.getenv("SENTIMENT_URL")
RESUME_URL = os.getenv("RESUME_URL")
IMAGE_URL = os.getenv("IMAGE_URL")


async def post_json(service_url: str, endpoint: str, payload: dict):
    url = f"{service_url}{endpoint}"

    async with httpx.AsyncClient(timeout=120.0) as client:
        for attempt in range(10):
            try:
                response = await client.post(url, json=payload)
                response.raise_for_status()
                return response.json()

            except httpx.ConnectError:
                print(f"Retry {attempt + 1}: Unable to connect to {url}")
                await asyncio.sleep(2)

            except httpx.HTTPStatusError as e:
                raise RuntimeError(
                    f"{url} returned {e.response.status_code}\n"
                    f"{e.response.text}"
                )

    raise RuntimeError(f"Cannot connect to {url}")


async def post_file(service_url: str, endpoint: str, files: dict):
    url = f"{service_url}{endpoint}"

    async with httpx.AsyncClient(timeout=120.0) as client:
        for attempt in range(10):
            try:
                response = await client.post(url, files=files)
                response.raise_for_status()
                return response.json()

            except httpx.ConnectError:
                print(f"Retry {attempt + 1}: Unable to connect to {url}")
                await asyncio.sleep(2)

            except httpx.HTTPStatusError as e:
                raise RuntimeError(
                    f"{url} returned {e.response.status_code}\n"
                    f"{e.response.text}"
                )

    raise RuntimeError(f"Cannot connect to {url}")