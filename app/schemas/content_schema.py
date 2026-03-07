from pydantic import BaseModel

class ContentCreate(BaseModel):
    topic_id: int
    content: str