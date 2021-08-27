import uvicorn
from data_generation import json_return
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return "Welcome to my app!"


@app.get("/json_stat")
def table_stat():
    return json_return()


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8501)
