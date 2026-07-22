from tools.internship_tool import search_internships

while True:

    query = input("\nAsk about internships (type exit to quit): ")

    if query.lower() == "exit":
        break

    internships = search_internships(query)

    print("\nResults\n")

    if not internships:
        print("No internships found.")
        continue

    for i, job in enumerate(internships, start=1):

        print("=" * 50)

        print(f"{i}. {job['company']}")

        print("Role      :", job["role"])
        print("Domain    :", job["domain"])
        print("Location  :", job["location"])
        print("Mode      :", job["mode"])
        print("Stipend   : ₹", job["stipend"])
        print("Branch    :", job["branch"])
        print("Skills    :", job["skills"])
        print("Apply Link:", job["apply_link"])