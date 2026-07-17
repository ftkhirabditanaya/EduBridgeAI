from tools.ats_scorer import calculate_ats_score

resume = """
Khirabdi Tanaya

B.Tech Electronics and Communication Engineering
Biomedical Engineering Specialization

Skills:
Python
Git
GitHub
Machine Learning
TensorFlow
SQL
Pandas
NumPy
Communication
Leadership

Projects:
Movie Recommendation System
EduBridge AI

Internship:
AI Research Intern
"""

result = calculate_ats_score(resume)

print(result)