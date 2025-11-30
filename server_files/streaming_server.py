from datetime import datetime, timedelta
import random
from time import sleep
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

app = FastAPI()

class Event(BaseModel):
    time: datetime
    action: str
    uri: str

def query_events(start_time: datetime):
    """Dummy query for events."""
    time = start_time
    for _ in range(10):
        sleep(1)
        time += timedelta(seconds=random.randint(10, 100))
        yield Event(time=time, action="GET", uri="/").model_dump_json() + '\n'

@app.get('/events', response_model=list[Event])
async def get_gen(start_time: datetime):
    events = query_events(start_time)
    return StreamingResponse(events, media_type="application/json")

@app.get('/')
def read_root():
    return {'message': 'It works!'}
