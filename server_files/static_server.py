import logging
from http import HTTPStatus

from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static_assets", StaticFiles(directory="static_assets"), name="static_assets")

logging.basicConfig(
    level=logging.INFO,
    datefmt='%Y-%m-%dT%H:%M:%S',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@app.get('/')
def read_root():
    return {'message': 'It Works!'}

@app.get('/static_assets/{file_path}')
def serve_static(file_path: str):
    logging.info('filename: %r', file_path)
    return RedirectResponse(
        url=('./static_assets/' + file_path),
        status_code=HTTPStatus.FOUND,
    )
