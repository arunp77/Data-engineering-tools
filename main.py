from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    itemid: int
    description: str
    owner: Optional[str] = None

app = FastAPI()

@app.post('/item')
def post_item(item: Item):
    return {
        'itemid': item.itemid
    }