from fastapi import FastAPI, Request
from routers import chat


app = FastAPI()
app.include_router(chat.router)

@app.get("/")
async def read_root(request: Request):
    return {"message": "Welcome to Speakeasy"}

