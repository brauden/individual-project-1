import io
import uvicorn
from enum import Enum
from data_generation import json_return, json_return_user_file
from fastapi import FastAPI, UploadFile, File


app = FastAPI()


class Options(str, Enum):
    """
    Enum subclass for enumerating possible
    options for including or excluding data stats.
    """
    all = "all"
    integer = "integer"
    floats = "float"
    number = "number"


@app.get("/")
def root():
    return "Welcome to my app! Check /docs for swagger API"


@app.get("/json_stat/{include}")
def table_stat(include: Options):
    """
    API for getting data description
    :param include: what to include in json_stat
    possible values: ["all", "integer", "floats", "number"]
    :return: json with data stats
    """
    return json_return(include)


@app.post("/csv_file_stat/{include}")
def user_file_stat(include: Options, file: UploadFile = File(...)):
    """

    :param include: what to include in json_stat.
    Possible values: ["all", "integer", "floats", "number"]
    :param file: upload csv file
    :return: json with user provided data stats
    """
    input_file = io.BytesIO(file.file.read())
    return json_return_user_file(input_file, include)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8501)
