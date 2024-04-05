from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi import Header
from fastapi import Request
from fastapi.responses import JSONResponse
import datetime

app = FastAPI()
class MyException(Exception):
    def __init__(self,                 
                 name : str,
                 date: str):
        self.name = name
        self.date = date
@app.exception_handler(MyException)
def MyExceptionHandler(
    request: Request,
    exception: MyException
    ):
    return JSONResponse(
        status_code=418,
        content={
            'url': str(request.url),
            'name': exception.name,
            'message': 'This error is my own', 
            'date': exception.date
        }
    )
@app.get('/my_custom_exception')
def get_my_custom_exception():
    raise MyException(
      name='my error',
      date=str(datetime.datetime.now())
      )