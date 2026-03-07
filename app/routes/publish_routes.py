from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.services.publish_service import export_dataset, push_to_github

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/publish")
def publish_dataset(db: Session = Depends(get_db)):

    export_dataset(db)

    push_to_github()

    return {"status": "dataset published"}