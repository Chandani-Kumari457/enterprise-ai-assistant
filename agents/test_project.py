import sqlite3

conn = sqlite3.connect("projects.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM projects")

data = cursor.fetchall()

print(data)

conn.close()