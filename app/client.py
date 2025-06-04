from dotenv import load_dotenv
import httpx
import os

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_KEY")
if not API_KEY:
    raise ValueError("API key for OpenWeather is not set.")


async def fetch_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
        if resp.status_code == httpx.codes.NOT_FOUND:
            # raise ValueError(f"City '{city}' not found.")
            print(f"City '{city}' not found.")
            return {}
        resp.raise_for_status()
        return resp.json()