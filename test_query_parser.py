from tools.query_parser import parse_internship_query

query = input("Ask anything:\n\n")

filters = parse_internship_query(query)

print("\nExtracted Filters\n")

print(filters)