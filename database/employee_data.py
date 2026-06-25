import sqlite3

conn = sqlite3.connect("employees.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    attendance INTEGER,
    salary INTEGER
)
""")

cursor.execute("""
INSERT OR IGNORE INTO employees
VALUES
(1,'Rahul','Developer',90,50000)
""")

cursor.execute("""
INSERT OR IGNORE INTO employees
VALUES
(2,'Priya','HR',85,45000)
""")

cursor.execute("""
INSERT OR IGNORE INTO employees
VALUES
(3,'Amit','Manager',95,70000)
""")

conn.commit()

print("Database Created Successfully")

conn.close()