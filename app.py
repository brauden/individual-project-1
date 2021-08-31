import uvicorn
from enum import Enum
from data_generation import json_return
from fastapi import FastAPI


app = FastAPI()


class Options(str, Enum):
    all = "all"
    integer = "integer"
    floats = "float"
    number = "number"


@app.get("/")
def root():
    return "Welcome to my app!"


@app.get("/json_stat/{include}")
def table_stat(include: Options):
    """
    API for getting data description
    :param include: possible values: ["all", "integer", "floats", "number"]
    :return: json with data stats
    """
    return json_return(include)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8501)
