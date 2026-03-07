import sqlite3
import subprocess
import os
from sqlalchemy.orm import Session
from app.database.models import Folder, Topic, GeneratedContent


DATASET_PATH = "dataset.db"


def export_dataset(db: Session):

    # remove old dataset so export is always fresh
    if os.path.exists(DATASET_PATH):
        os.remove(DATASET_PATH)

    conn = sqlite3.connect(DATASET_PATH)
    cursor = conn.cursor()

    # create tables
    cursor.execute("""
    CREATE TABLE folders(
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        parent_id INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE topics(
        id INTEGER PRIMARY KEY,
        name TEXT,
        folder_id INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE generated_content(
        id INTEGER PRIMARY KEY,
        topic_id INTEGER,
        content TEXT
    )
    """)

    # fetch data from main database
    folders = db.query(Folder).all()
    topics = db.query(Topic).all()
    content = db.query(GeneratedContent).all()

    # insert folders
    for f in folders:
        cursor.execute(
            "INSERT INTO folders VALUES (?, ?, ?, ?)",
            (f.id, f.name, f.category, f.parent_id)
        )

    # insert topics
    for t in topics:
        cursor.execute(
            "INSERT INTO topics VALUES (?, ?, ?)",
            (t.id, t.name, t.folder_id)
        )

    # insert generated content
    for c in content:
        cursor.execute(
            "INSERT INTO generated_content VALUES (?, ?, ?)",
            (c.id, c.topic_id, c.content)
        )

    conn.commit()

    # force SQLite to rebuild file so Git detects change
    cursor.execute("VACUUM")

    conn.close()

def push_to_github():

    # 1️⃣ pull latest repo first
    subprocess.run([
        "git",
        "pull",
        "--rebase",
        "origin",
        "main"
    ])

    # 2️⃣ add dataset
    subprocess.run([
        "git",
        "add",
        "-f",
        "dataset.db"
    ])

    # 3️⃣ commit
    subprocess.run([
        "git",
        "commit",
        "--allow-empty",
        "-m",
        "dataset update"
    ])

    # 4️⃣ push
    subprocess.run([
        "git",
        "push",
        "origin",
        "main"
    ])
