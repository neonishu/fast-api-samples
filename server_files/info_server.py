from fastapi import FastAPI
import os
from datetime import datetime

VERSION = "0.1.0"

app = FastAPI()
"""
export USER=testuser
OR simply run `USER=testuser fastapi run info_server.py`
and it will export the USER env variable
"""
@app.get("/info")
def info():
    return {
        "version": VERSION,
        "time": datetime.now().isoformat(),
        "user": os.getenv("USER"),
    }
