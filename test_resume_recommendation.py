from tools.recommendation_resume import recommend_from_resume

results = recommend_from_resume("sample_resume.txt")

print()

print("=" * 70)
print("TOP INTERNSHIP RECOMMENDATIONS")
print("=" * 70)

for job in results:

    print()

    print(job["company"])

    print(job["role"])

    print("Resume Match :", job["score"], "%")

    print()

    print("Matched Skills")

    for skill in job["matched_skills"]:

        print("✓", skill)

    print()

    print("Missing Skills")

    for skill in job["missing_skills"]:

        print("-", skill)

    print("-" * 70)