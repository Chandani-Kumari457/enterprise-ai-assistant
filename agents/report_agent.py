import sqlite3
from config.gemini_config import model

def report_agent(query):

    conn = sqlite3.connect("employees.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM employees"
    )

    employees = cursor.fetchall()

    conn.close()

    total = len(employees)

    avg_attendance = sum(
        emp[3] for emp in employees
    ) / total

    best_employee = max(
        employees,
        key=lambda x: x[3]
    )

    lowest_employee = min(
        employees,
        key=lambda x: x[3]
    )

    prompt = f"""
    Create a professional employee performance report.

    Total Employees: {total}

    Average Attendance: {avg_attendance:.2f}%

    Top Performer:
    {best_employee[1]}
    Attendance: {best_employee[3]}%

    Lowest Performer:
    {lowest_employee[1]}
    Attendance: {lowest_employee[3]}%

    Give:
    - Summary
    - Insights
    - Recommendations
    """

    response = model.generate_content(
        prompt
    )

    return response.text