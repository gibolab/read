from fastapi import FastAPI
from app.routes.ai_routes import router as ai_router
from app.database.db import engine
from app.database.models import Base
from fastapi.middleware.cors import CORSMiddleware
from app.routes.folder_routes import router as folder_router
from app.routes.publish_routes import router as publish_router

app = FastAPI(title="AI Paragraph Engine")

Base.metadata.create_all(bind=engine)

app.include_router(ai_router, prefix="/ai")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for testing only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(folder_router, prefix="/data")

app.include_router(publish_router, prefix="/publish")