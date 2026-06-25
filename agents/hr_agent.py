import sqlite3

def hr_agent(query):

    conn = sqlite3.connect("employees.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")

    data = cursor.fetchall()

    conn.close()

    return data