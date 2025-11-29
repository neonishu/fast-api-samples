from fastapi import FastAPI
import asyncio
from time import sleep

app = FastAPI()

@app.get("/")
def read_root():
    return {'message': 'It Works!'}

"""
Non async handler, performs the system sleep
Read more on: https://docs.python.org/3/library/asyncio.html

Test using a utility called hey(I tested on mac)
hey -c 10 -n 10 http://localhost:8000/sleep/sys
"""
@app.get('/sleep/sys')
def nsys_sleep():
    sleep(1)
    return {'message': 'I slept for just 1 second'}

"""
Async handler, but performs the system sleep
IT IS A NO-NO, it will block every request in the pipeline using system sleep
Read more on: https://docs.python.org/3/library/asyncio.html

Test using a utility called hey(I tested on mac)
hey -c 10 -n 10 http://localhost:8000/sleep/async-sys
"""
@app.get('/sleep/async-sys')
async def sys_sleep():
    sleep(1)
    return {'message': 'I slept for just 1 second, blocking everything'}

"""
Async handler, performs the asyncio sleep,
Non blocking for concurrent requests
Read more on: https://docs.python.org/3/library/asyncio.html

Test using a utility called hey(I tested on mac)
hey -c 10 -n 10 http://localhost:8000/sleep/async-aio
"""
@app.get('/sleep/async-aio')
async def aio_sleep():
    await asyncio.sleep(1)
    return {'message': 'I slept for just 1 second, but async'}
