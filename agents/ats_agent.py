from google.adk.agents.llm_agent import Agent
from google.adk.tools import FunctionTool

from tools.ats_scorer import calculate_ats_score
from tools.resume_parser import extract_text
from tools.resume_analyzer import analyze_resume

ats_tool = FunctionTool(calculate_ats_score)
resume_parser_tool = FunctionTool(extract_text)
resume_analyzer_tool = FunctionTool(analyze_resume)

ats_agent = Agent(
    name="ats_agent",

    model="gemini-2.5-flash",

    description="ATS resume scoring specialist",

    instruction="""
You are EduBridge AI's ATS Scoring Expert.

When a user wants their resume scored or analyzed for ATS compatibility:

Step 1: Extract text from the resume using the resume parser.

Step 2: Analyze the resume to identify skills, education, and experience.

Step 3: Calculate the ATS score using the ATS scorer tool.

After getting the results:

1. Show the ATS Score prominently.
2. List matched technical skills.
3. List matched soft skills.
4. Show strengths.
5. Show missing skills the student should learn.
6. Give actionable suggestions.

Always use headings and bullet points.
Never answer in one paragraph.
""",

    tools=[ats_tool, resume_parser_tool, resume_analyzer_tool],
)
