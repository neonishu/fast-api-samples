from http import HTTPStatus
from fastapi import FastAPI, HTTPException
from datetime import datetime

app = FastAPI()

"""
An example of how params can be accepted,
simple returns the count of days between 2 dates.
"""
@app.get('/days_count')
def days_count(start: datetime, end: datetime):
    if start >= end:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail="Start date must be before end date"
        )
    # calculate the difference in days
    delta = end - start
    return {'days_count': delta.days}
