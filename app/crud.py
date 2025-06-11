"""
CRUD = Create, Read, Update, Delete
This module contains  all DB functions:
(functions to interact with the weather data in the database.)
"""
from datetime import datetime, timezone

from app.db import db


def _printable_record(record: dict):
    return {
        "city": record["city"],
        "temp": record["temp"],
        "source": record["source"],
        "timestamp": record["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),
    }


async def save_record(data: dict):
    """
    Saves weather data to the database.
    makes sure to save the data with a timestamp.
        `weather> db.forecasts.insertOne(
                  {city: "Kofiko", temp: 11, source: "manual" , "timestamp": ISODate obj, raw_data: {...}})`
    """
    print(f'Get weather data: {data}')
    record = {
        "city": data.get('name'),
        "temp": data.get('main', {}).get('temp'),
        "source": 'OpenWeather',
        "timestamp": datetime.now(timezone.utc),
        "_raw_data": data  # Store the full data for future reference
    }
    await db.weather.insert_one(record)
    print(f"Saved to MongoDB: { _printable_record(record) }")


async def get_updated_record(city: str):
    print(f'Get latest weather for city: {city}')
    record = await db.weather.find_one({"city": city}, sort=[("timestamp", -1)])
    if not record:
        print(f"No records found for city: {city}")
        return None
    record.pop('_id', None)  # Remove MongoDB's ObjectId field
    record.pop('_raw_data', None)  # Remove the raw data if not needed in the response
    return record


async def delete_all_records():
    print('Delete all weather records')
    result = await db.weather.delete_many({})
    print(f'Deleted {result.deleted_count} records from MongoDB')
    return {"status": "ok", "deleted_count": result.deleted_count}
