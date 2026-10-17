import os
import pandas as pd

from tools.resume_parser import extract_text
from tools.resume_analyzer import analyze_resume


DATABASE_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "database",
    "internships.csv"
)


def load_database():
    return pd.read_csv(DATABASE_PATH)


def calculate_resume_score(resume_data, internship):

    score = 0

    matched_skills = []
    missing_skills = []

    resume_skills = [
        skill.lower()
        for skill in resume_data["Skills"]
    ]

    internship_skills = [
        skill.strip().lower()
        for skill in internship["skills"].split(",")
    ]

    # --------------------------
    # Skills (50)
    # --------------------------

    matched = 0

    for skill in internship_skills:

        if skill in resume_skills:

            matched += 1
            matched_skills.append(skill.title())

        else:

            missing_skills.append(skill.title())

    if internship_skills:

        score += int(
            (matched / len(internship_skills)) * 50
        )

    # --------------------------
    # Education (20)
    # --------------------------

    if resume_data["Education"]:

        score += 20

    # --------------------------
    # Projects (20)
    # --------------------------

    if resume_data["Projects"]:

        score += 20

    # --------------------------
    # Experience (10)
    # --------------------------

    if resume_data["Experience"]:

        score += 10

    return {

        "company": internship["company"],

        "role": internship["role"],

        "domain": internship["domain"],

        "location": internship["location"],

        "stipend": internship["stipend"],

        "score": score,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills

    }


def recommend_from_resume(resume_path):

    resume_text = extract_text(resume_path)

    resume_data = analyze_resume(resume_text)

    df = load_database()

    recommendations = []

    for _, internship in df.iterrows():

        result = calculate_resume_score(

            resume_data,

            internship.to_dict()

        )

        recommendations.append(result)

    recommendations.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return recommendations