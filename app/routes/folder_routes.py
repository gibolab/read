from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.database import crud
from app.schemas.folder_schema import FolderCreate, TopicCreate
from app.schemas.content_schema import ContentCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/folder")
def create_folder(data: FolderCreate, db: Session = Depends(get_db)):
    return crud.create_folder(db, data.name, data.category, data.parent_id)


@router.get("/folder")
def get_folders(parent_id: int | None = None, db: Session = Depends(get_db)):
    return crud.get_folders(db, parent_id)


@router.delete("/folder/{folder_id}")
def delete_folder(folder_id: int, db: Session = Depends(get_db)):
    crud.delete_folder(db, folder_id)
    return {"status": "deleted"}


@router.post("/topic")
def create_topic(data: TopicCreate, db: Session = Depends(get_db)):
    return crud.create_topic(db, data.name, data.folder_id)


@router.get("/topic/{folder_id}")
def get_topics(folder_id: int, db: Session = Depends(get_db)):
    return crud.get_topics(db, folder_id)


@router.delete("/topic/{topic_id}")
def delete_topic(topic_id: int, db: Session = Depends(get_db)):
    crud.delete_topic(db, topic_id)
    return {"status": "deleted"}

@router.post("/content")
def save_content(data: ContentCreate, db: Session = Depends(get_db)):
    return crud.save_generated_content(db, data.topic_id, data.content)


@router.get("/content/{topic_id}")
def get_content(topic_id: int, db: Session = Depends(get_db)):
    return crud.get_generated_content(db, topic_id)