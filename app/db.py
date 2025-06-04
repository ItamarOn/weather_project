# from motor.motor_asyncio import AsyncIOMotorClient
import os

# MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
# client = AsyncIOMotorClient(MONGO_URL)
# db = client.weather_db

async def init_db():
    print('DB connection initialized')
    #await db.weather.create_index("timestamp")
