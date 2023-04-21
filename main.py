from fastapi import FastAPI
from APIs.Bills import billAPI
from APIs.Test import testAPI

app = FastAPI()

app.include_router(billAPI.router)
app.include_router(testAPI.router)

@app.get("/")
async def root():
    return {"message": "Hello Visual Mate"}


