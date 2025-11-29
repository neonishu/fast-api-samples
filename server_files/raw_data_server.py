from fastapi import FastAPI, Request, HTTPException
from PIL import Image
from io import BytesIO
from http import HTTPStatus

MAX_IMAGE_SIZE = 2 * 1024 * 1024 # 2MB

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'It works!'}

@app.post('/get_details')
async def get_size(request: Request):
    size = int(request.headers.get('Content-Length') or 0)

    if not size:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Content-Length header must have a non-zero value'
        )
    if size > MAX_IMAGE_SIZE:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=f'File size is too large. Max size is {MAX_IMAGE_SIZE} bytes'
        )
    data = await request.body()
    io = BytesIO(data)
    image = Image.open(io)

    return {'width': image.width, 'height': image.height, 'type': image.format}
