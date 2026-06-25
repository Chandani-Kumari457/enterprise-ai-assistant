import sqlite3

def analytics_agent(query):

    conn = sqlite3.connect("employees.db")

    cursor = conn.cursor()

    cursor.execute("SELECT name, attendance FROM employees")

    data = cursor.fetchall()

    conn.close()

    total = 0

    for employee in data:
        total += employee[1]

    average = total / len(data)

    highest = max(data, key=lambda x: x[1])

    lowest = min(data, key=lambda x: x[1])

    return f"""
Average Attendance: {average:.2f}%

Highest Attendance:
{highest[0]} ({highest[1]}%)

Lowest Attendance:
{lowest[0]} ({lowest[1]}%)
"""