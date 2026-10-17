from tools.internship_tool import search_internships

while True:

    query = input("\nAsk about internships (type exit to quit): ")

    if query.lower() == "exit":
        break

    internships = search_internships(query)

    if not internships:
        print("\nNo internships found.")
        continue

    print("\nRecommended Internships\n")

    for i, job in enumerate(internships, start=1):

        print("=" * 65)

        print(f"#{i} {job['company']}")
        print(job["role"])

        print("\n⭐ Match Score :", job["match_score"], "%")

        print("\nWhy Recommended")

        if job["reasons"]:
            for reason in job["reasons"]:
                print(reason)
        else:
            print("No specific match found.")

        if job["missing"]:
            print("\nMissing Criteria")

            for item in job["missing"]:
                print("•", item)

        print("\nLocation :", job["location"])
        print("Mode     :", job["mode"])
        print("Branch   :", job["branch"])
        print("Stipend  : ₹", job["stipend"])
        print("Skills   :", job["skills"])
        print("Apply    :", job["apply_link"])

        print("=" * 65)