from tools.recommendation_engine import calculate_match_score

filters = {

    "domain": "AI",

    "location": "Bangalore",

    "mode": "Hybrid",

    "branch": "ECE",

    "minimum_stipend": 70000
}

internship = {

    "company": "Google",

    "role": "Software Engineering Intern",

    "domain": "AI",

    "location": "Bangalore",

    "mode": "Hybrid",

    "stipend": 80000,

    "branch": "CSE/ECE"
}

result = calculate_match_score(filters, internship)

print(result)