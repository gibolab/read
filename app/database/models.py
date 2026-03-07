# # app/database/models.py

# from sqlalchemy import Column, Integer, String, ForeignKey, Text
# from sqlalchemy.orm import relationship
# from app.database.db import Base

# class Folder(Base):
#     __tablename__ = "folders"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     category = Column(String)
#     parent_id = Column(Integer, ForeignKey("folders.id"), nullable=True)

#     children = relationship("Folder")

# class Topic(Base):
#     __tablename__ = "topics"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     folder_id = Column(Integer, ForeignKey("folders.id"))

# class GeneratedContent(Base):
#     __tablename__ = "generated_content"

#     id = Column(Integer, primary_key=True, index=True)
#     content = Column(Text)
#     topic_id = Column(Integer, ForeignKey("topics.id"))

from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database.db import Base


class Folder(Base):
    __tablename__ = "folders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(String)
    parent_id = Column(Integer, ForeignKey("folders.id"), nullable=True)

    children = relationship(
        "Folder",
        cascade="all, delete"
    )

    topics = relationship(
        "Topic",
        cascade="all, delete"
    )


class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    folder_id = Column(Integer, ForeignKey("folders.id"))

    generated_content = relationship(
        "GeneratedContent",
        cascade="all, delete"
    )


class GeneratedContent(Base):
    __tablename__ = "generated_content"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    topic_id = Column(Integer, ForeignKey("topics.id"))