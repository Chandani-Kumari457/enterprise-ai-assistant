import sqlite3

def get_employee_count():

    conn = sqlite3.connect("employees.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM employees"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count


def get_average_attendance():

    conn = sqlite3.connect("employees.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT AVG(attendance) FROM employees"
    )

    avg = cursor.fetchone()[0]

    conn.close()

    return round(avg, 2)


def get_project_count():

    conn = sqlite3.connect("projects.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM projects"
    )

    count = cursor.fetchone()[0]

    conn.close()


    return count
import pandas as pd
def get_employee_dataframe():

    df = pd.read_csv(
        "datasets/WA_Fn-UseC_-HR-Employee-Attrition.csv"
    )

    return df

def get_top_performer():

    conn = sqlite3.connect("employees.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, attendance FROM employees ORDER BY attendance DESC LIMIT 1"
    )

    result = cursor.fetchone()

    conn.close()

    return result
