import asyncio
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager

from app.client import fetch_weather
from app.db import init_db
from app.schema import WeatherRecordOut,  WeatherRecordHistoryOut
from app.crud import save_record, get_updated_record, delete_all_records, get_city_records_history



@asynccontextmanager
async def lifespan(app: FastAPI):
    """ background task starts at startup """
    from app.services.fetcher import periodic_fetch_weather

    await init_db()
    task = asyncio.create_task(periodic_fetch_weather())
    yield
    task.cancel()
    # consider `suppress(asyncio.CancelledError): await task`

app = FastAPI(lifespan=lifespan)


@app.get("/weather", response_model=WeatherRecordOut)
async def get_weather(city : str ="Tel Aviv") -> WeatherRecordOut:
    if not (last_record := await get_updated_record(city)):
        raise HTTPException(status_code=404, detail=f"No weather data in DB for city '{city}'")
    return last_record


@app.post("/weather/fetch")
async def fetch_and_store(city : str ="Tel Aviv"):
    print(f"🌐 fetching weather for {city}")
    data = await fetch_weather(city=city)
    await save_record(data)
    print(f"🌐 done fetching weather for {city}")
    return


@app.get("/weather/history", response_model=WeatherRecordHistoryOut)
async def get_weather_history(city: str = "Tel Aviv") -> WeatherRecordHistoryOut:
    records = await get_city_records_history(city)
    if not records:
        raise HTTPException(status_code=404, detail=f"No history found for city '{city}'")
    return records


@app.delete("/weather")
async def delete_all_weather():
    return await delete_all_records()