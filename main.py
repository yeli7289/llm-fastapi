from fastapi import FastAPI, Request
from mangum import Mangum


app = FastAPI()

@app.get("/")
async def read_root(request: Request):
    return {"Hello": "World"}

# handler = Mangum(app)
