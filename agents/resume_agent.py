from google.adk.agents import Agent

from tools.resume_parser import extract_text
from tools.resume_analyzer import analyze_resume
from tools.ats_scorer import calculate_ats_score
from tools.internship_tool import search_internships
from tools.career_tool import search_careers


resume_agent = Agent(
    name="resume_agent",

    model="gemini-2.5-flash",

    description="Professional Resume Analysis Specialist",

    instruction="""
You are EduBridge AI's Resume Expert.

Whenever a user uploads or provides a resume:

Step 1
Extract resume information using Resume Parser.

Step 2
Analyze the resume.

Step 3
Calculate ATS Score.

Step 4
Suggest missing skills.

Step 5
Recommend internships.

Step 6
Recommend career paths.

Finally produce a beautiful report.

Use proper headings.

Use bullet points.

Use tables whenever useful.

Never answer in one paragraph.
""",

    tools=[
        extract_text,
        analyze_resume,
        calculate_ats_score,
        search_internships,
        search_careers,
    ],
)