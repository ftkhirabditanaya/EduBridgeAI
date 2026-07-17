from tools.career_tool import search_by_stream
from tools.college_tool import search_by_course
from tools.internship_tool import search_by_skill
from tools.scholarship_tool import search_by_amount

print("=== Careers ===")
print(search_by_stream("PCB"))

print("\n=== Colleges ===")
print(search_by_course("Bioinformatics"))

print("\n=== Internships ===")
print(search_by_skill("Python"))

print("\n=== Scholarships ===")
print(search_by_amount(50000))