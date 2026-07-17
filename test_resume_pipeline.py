from tools.resume_parser import extract_text
from tools.resume_analyzer import analyze_resume
from tools.ats_scorer import calculate_ats_score

resume = extract_text("sample_resume.txt")

analysis = analyze_resume(resume)

ats = calculate_ats_score(resume)

print("=" * 60)
print("RESUME ANALYSIS")
print("=" * 60)

for key, value in analysis.items():
    print(f"\n{key}")
    print(value)

print("\n" + "=" * 60)
print("ATS REPORT")
print("=" * 60)

for key, value in ats.items():
    print(f"\n{key}")
    print(value)