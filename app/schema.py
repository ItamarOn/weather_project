from pydantic import BaseModel
from datetime import datetime

class WeatherRecordOut(BaseModel):
    city: str
    temp: float
    source: str
    timestamp: datetime

class WeatherRecordHistoryOut(BaseModel):
    city: str
    historic_temps: list
    latest_record: datetime
    earliest_record: datetime