from fastapi import FastAPI
import time
import asyncio
app = FastAPI()
def wait_sync():
    time.sleep(10)
    return True
async def wait_async():
    await asyncio.sleep(10)
    return True
@app.get('/sync')
def get_sync():
    wait_sync()
    return {
        'message': 'synchronous'
    }
@app.get('/async')
async def get_async():
    wait_async()
    return {
        'message': 'asynchronous'
    }