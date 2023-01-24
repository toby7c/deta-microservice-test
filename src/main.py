from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Test 12345"}

@app.get("/httpbin")
async def httpbin():
    return requests.get("https://httpbin.org/uuid").json().get("uuid", "Uh oh.")
