import sqlite3

conn = sqlite3.connect("projects.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS projects(
    id INTEGER PRIMARY KEY,
    project_name TEXT,
    status TEXT,
    progress INTEGER
)
""")

cursor.execute("""
INSERT OR IGNORE INTO projects
VALUES
(1,'Enterprise AI Assistant','In Progress',80)
""")

conn.commit()

print("Project Database Created")

conn.close()