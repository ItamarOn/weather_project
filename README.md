## Weather Project

### description
This project demonstrates an async architecture designed for performance (via FastAPI and httpx), scalability (modular, stateless services), and observability (structured logs and clean error handling).

### purpose
This project was designed as a hands-on exercise in
building asynchronous Python services using modern tools and best practices. 
While the actual task - fetching and storing weather forecasts - 
could be implemented synchronously, 
the goal here is to simulate real-world scenarios where:
API calls may be slow or numerous
Non-blocking I/O is required for performance
The service may need to scale to support multiple concurrent requests

By using FastAPI, httpx, and Motor (async MongoDB driver), the project demonstrates:
How to structure and manage an async-first backend
Integration with external APIs in a non-blocking way
Asynchronous database interaction with MongoDB
Clean project structure, modular code, and observability foundations

Bottom line: The asynchronous architecture here is a deliberate choice
to learn and master advanced backend patterns, 
not because the domain problem strictly.

# API App
```commandline
source weather_proj_env/bin/activate
uvicorn app.main:app --reload
```
🌐 http://127.0.0.1:8000/docs/

# Mongo Shell
```commandline
mongosh mongodb://localhost:27017
use weather
db.weather.find().pretty()
db.forecasts.find().sort({ temp: -1 })

#delete
docker rm -f weather-mongo
docker run -d --name weather-mongo -p 27017:27017 mongo:latest
```
❤️
✅
✨
🔥
😭
🫶
⭐
😂
🥹