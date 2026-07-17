TECHNICAL_SKILLS = [
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

SOFT_SKILLS = [
    "communication",
    "leadership",
    "teamwork",
    "problem solving",
    "critical thinking",
    "adaptability",
]


def calculate_ats_score(text):

    lower = text.lower()

    technical_found = []

    for skill in TECHNICAL_SKILLS:
        if skill in lower:
            technical_found.append(skill)

    soft_found = []

    for skill in SOFT_SKILLS:
        if skill in lower:
            soft_found.append(skill)

    score = len(technical_found) * 5 + len(soft_found) * 4

    score = min(score, 100)

    missing = [
        skill
        for skill in TECHNICAL_SKILLS
        if skill not in technical_found
    ]

    strengths = []

    if len(technical_found) >= 6:
        strengths.append("Strong technical foundation")

    if "git" in technical_found:
        strengths.append("Version control knowledge")

    if "tensorflow" in technical_found:
        strengths.append("AI/ML framework experience")

    suggestions = []

    if "flask" not in technical_found:
        suggestions.append("Learn Flask")

    if "react" not in technical_found:
        suggestions.append("Learn React")

    if "django" not in technical_found:
        suggestions.append("Learn Django")

    return {
        "ATS Score": score,
        "Technical Skills": technical_found,
        "Soft Skills": soft_found,
        "Strengths": strengths,
        "Missing Skills": missing,
        "Suggestions": suggestions,
    }