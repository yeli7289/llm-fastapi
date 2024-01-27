from fastapi import APIRouter
from pydantic import BaseModel


class ChatRequest(BaseModel):
    input: str


class ChatResponse(BaseModel):
    message: str
    
router = APIRouter()
@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    return {"message": f"hello this is speakeasy ai! {request.input}"}
