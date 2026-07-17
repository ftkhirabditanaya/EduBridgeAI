import re

TECH_SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "tensorflow",
    "pytorch",
    "machine learning",
    "deep learning",
    "numpy",
    "pandas",
    "opencv",
    "git",
    "github",
    "flask",
    "django",
    "html",
    "css",
    "javascript",
    "react",
    "node",
]

EDUCATION_KEYWORDS = [
    "b.tech",
    "b.e",
    "bachelor",
    "m.tech",
    "m.e",
    "master",
    "phd",
    "diploma",
]

def analyze_resume(text):

    result = {}

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    # Name
    result["Name"] = lines[0] if lines else "Not Found"

    # Email
    email = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    result["Email"] = email.group() if email else "Not Found"

    # Phone
    phone = re.search(r'\b\d{10}\b', text)
    result["Phone"] = phone.group() if phone else "Not Found"

    # Skills
    lower = text.lower()

    skills = []

    for skill in TECH_SKILLS:

        if skill in lower:
            skills.append(skill.title())

    result["Skills"] = skills

    # Education

    education = []

    for keyword in EDUCATION_KEYWORDS:

        if keyword in lower:
            education.append(keyword.upper())

    result["Education"] = education

    # Projects

    projects = []

    for line in lines:

        if "project" in line.lower():
            continue

        if "densenet" in line.lower():

            projects.append(line)

        elif "smart" in line.lower():

            projects.append(line)

    result["Projects"] = projects

    # Experience

    experience = []

    for line in lines:

        if "ieee" in line.lower():

            experience.append(line)

        elif "intern" in line.lower():

            experience.append(line)

        elif "team" in line.lower():

            experience.append(line)

    result["Experience"] = experience

    return result