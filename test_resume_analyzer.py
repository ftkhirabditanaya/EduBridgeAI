from tools.resume_parser import extract_text
from tools.resume_analyzer import analyze_resume

text = extract_text("sample_resume.txt")

data = analyze_resume(text)

for key, value in data.items():
    print(f"\n{key}")
    print(value)