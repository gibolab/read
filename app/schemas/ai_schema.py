from pydantic import BaseModel

class AIRequest(BaseModel):
    topic: str
    category: str

class AIResponse(BaseModel):
    content: str