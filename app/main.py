from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager

from app.client import fetch_weather
from app.db import init_db
from app.crud import save_record, get_updated_record, delete_all_records


@asynccontextmanager
async def lifespan(app: FastAPI):
    """ background task starts at startup """
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/weather")
async def get_weather(city : str ="Tel Aviv"):
    if not (last_record := await get_updated_record(city)):
        raise HTTPException(status_code=404, detail=f"No weather data in DB for city '{city}'")
    return last_record


@app.post("/weather/fetch")
async def fetch_and_store(city : str ="Tel Aviv"):
    data = await fetch_weather(city=city)
    await save_record(data)
    return {"status": "ok"}

@app.delete("/weather")
async def delete_all_weather():
    return await delete_all_records()