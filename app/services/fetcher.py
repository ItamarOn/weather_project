import os
import asyncio
from dotenv import load_dotenv

from app.crud import get_all_cities
from app.main import fetch_and_store

load_dotenv()

FETCH_MINUTE_LOOP = int(os.getenv("FETCH_MINUTE_LOOP", 1))


async def periodic_fetch_weather():
    print("periodic_fetch_weather started...")
    cities = []
    counter = 0
    while True:
        print(f'c: {counter}')

        if counter % (100 * FETCH_MINUTE_LOOP) == 0:
            try:
                print("🌀 about to call get_all_cities()")
                cities = await get_all_cities()
                print(f"⏰ Refresh cities.... {len(cities)} cities found")
            except Exception as e:
                print(f"Error during scheduled fetch cities: {e}")

        try:
            print(f"⏰ Fetching weather for {cities}")
            await asyncio.gather(*(fetch_and_store(city) for city in cities))
        except Exception as e:
            print(f"Error during scheduled fetch: {e}")

        await asyncio.sleep(60 * FETCH_MINUTE_LOOP)
        counter += 1
