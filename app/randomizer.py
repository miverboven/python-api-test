from fastapi import FastAPI
from random import randint

app = FastAPI()

#12345

@app.get("/percentage")
async def get_random_percentage():
    return {'percentage': randint(0, 100)}
