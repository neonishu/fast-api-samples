from http import HTTPStatus
from io import BytesIO
from PIL import Image
from fastapi import FastAPI, Request, Response, HTTPException

app = FastAPI()

MAX_IMAGE_SIZE = 2 * 1024 * 1024 # 2MB

@app.get('/')
def read_root():
    return {'message': 'It works!'}
"""
This resizes the given image, if format not found, it takes JPEG by default
"""
@app.post('/resize')
async def resize_image(width: int, height: int, request: Request):
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
    if height <= 0 or width < 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Height and width must be positive'
        )
    data = await request.body()
    io = BytesIO(data)
    image = Image.open(io)
    original_format = image.format or 'JPEG'

    image = image.resize((width, height))
    out = BytesIO()
    image.save(out, format=original_format)
    return Response(
        content=out.getvalue(),
        status_code=HTTPStatus.OK,
        media_type=f"image/{original_format.lower()}"
    )
