import sqlite3

def project_agent(query):

    conn = sqlite3.connect("projects.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM projects")

    project = cursor.fetchone()

    conn.close()

    return f"""
Project Name: {project[1]}

Status: {project[2]}

Progress: {project[3]}%
"""