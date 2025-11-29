from datetime import datetime, timedelta
from fastapi import FastAPI
from pydantic import BaseModel, field_serializer

app = FastAPI()

class TimeResponse(BaseModel):
    timediff: timedelta

    @field_serializer("timediff")
    def serialize_timedelta(self, v: timedelta) -> str:
        return str(v)

@app.get('/')
def read_root():
    return {'message': 'It works!'}

@app.get('/timediff')
def get_time(start: datetime, end: datetime) -> TimeResponse:
    return TimeResponse(timediff=(end - start))
