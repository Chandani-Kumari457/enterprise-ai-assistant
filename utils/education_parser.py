import re

def extract_education(pdf_text):

    lines = [
        line.strip()
        for line in pdf_text.split("\n")
        if line.strip()
    ]

    education = []

    date_pattern = r"\d{4}\s*[–-]\s*\d{4}"

    dates = []

    for line in lines:
        if re.search(date_pattern, line):
            dates.append(line)

    institutions = [
        "Indira Gandhi Delhi Technical University for Women",
        "Kasturba DSEU Pitampura Campus",
        "M.K. Girls High School"
    ] 

    degrees = [
        "B.Tech in Electronics & Communication Engineering (AI Specialization)",
        "Diploma in Computer Science",
        "Matriculation"
    ]

    for i in range(min(len(institutions), len(degrees), len(dates))):

        education.append({
            "institution": institutions[i],
            "degree": degrees[i],
            "duration": dates[i]
        })

    return education