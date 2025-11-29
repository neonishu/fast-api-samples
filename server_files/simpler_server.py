from fastapi import FastAPI

"""
Bare minimum implementation with FastAPI
IT runs the server on port 8000
just call `fastapi dev ./simpler_server.py`
"""

app = FastAPI()

@app.get("/")
def read_root():
    return {'message': 'It Works!'}

@app.get("/health")
def health():
    return {'status': 'ok'}
