from fastapi import FastAPI
import uvicorn

app = FastAPI()

"""
This is an example where you can manually run the server from inside
the file instead of calling `fastapi run` command to run the server
Just do `python ./manual_server.py` and it will run the server on 8001 port
The downside is, it will not reload the code of the server
"""

@app.get("/")
def read_root():
    return {'message': 'It Works!'}

@app.get("/health")
def health():
    return {'status': 'ok'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
