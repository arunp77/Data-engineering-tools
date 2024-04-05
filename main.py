from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi import Header

app = FastAPI()
data = [1, 2, 3, 4, 5]
@app.get('/data')
def get_data(index):
    return {
        'data': data[int(index)]
    }