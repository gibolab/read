from pydantic import BaseModel

class FolderCreate(BaseModel):
    name: str
    category: str
    parent_id: int | None = None


class TopicCreate(BaseModel):
    name: str
    folder_id: int