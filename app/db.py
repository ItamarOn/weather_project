from dotenv import load_dotenv
import os
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client["weather"]

async def init_db():
    print('DB connection initialized')
    await db.weather.create_index("timestamp") # why?
