"""
CRUD = Create, Read, Update, Delete
This module contains  all DB functions:
(functions to interact with the weather data in the database.)
"""
# from app.db import db
import datetime

async def save_weather(data: dict):
    print(f'Saving weather data: {data}')
    # data["timestamp"] = datetime.datetime.utcnow()
    # await db.weather.insert_one(data)

async def get_latest_weather():
    print('get_latest_weather Fetching latest weather data')
    # doc = await db.weather.find_one(sort=[("timestamp", -1)])
    # return doc