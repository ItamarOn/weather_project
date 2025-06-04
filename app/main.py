from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.client import fetch_weather
from app.db import init_db
from app.crud import save_weather, get_latest_weather


@asynccontextmanager
async def lifespan(app: FastAPI):
    """ background task starts at statrup """
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/weather")
async def get_weather():
    return await get_latest_weather()

@app.post("/weather/fetch")
async def fetch_and_store(city : str ="Tel Aviv"):
    data = await fetch_weather(city=city)
    await save_weather(data)
    return {"status": "ok"}
