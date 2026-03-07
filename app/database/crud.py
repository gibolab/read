from app.database.models import Folder, Topic, GeneratedContent


def create_folder(db, name, category, parent_id=None):
    folder = Folder(name=name, category=category, parent_id=parent_id)
    db.add(folder)
    db.commit()
    db.refresh(folder)
    return folder


def get_folders(db, parent_id=None):
    return db.query(Folder).filter(Folder.parent_id == parent_id).all()


def delete_folder(db, folder_id):
    folder = db.query(Folder).filter(Folder.id == folder_id).first()
    db.delete(folder)
    db.commit()


def create_topic(db, name, folder_id):
    topic = Topic(name=name, folder_id=folder_id)
    db.add(topic)
    db.commit()
    db.refresh(topic)
    return topic


def get_topics(db, folder_id):
    return db.query(Topic).filter(Topic.folder_id == folder_id).all()


def delete_topic(db, topic_id):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    db.delete(topic)
    db.commit()

def save_generated_content(db, topic_id, content):
    entry = GeneratedContent(topic_id=topic_id, content=content)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def get_generated_content(db, topic_id):
    return db.query(GeneratedContent).filter(
        GeneratedContent.topic_id == topic_id
    ).all()