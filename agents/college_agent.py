from google.adk.agents.llm_agent import Agent
from google.adk.tools import FunctionTool

from tools.college_tool import search_colleges

college_tool = FunctionTool(search_colleges)

college_agent = Agent(
    name="college_agent",

    model="gemini-2.5-flash",

    description="College recommendation specialist",

    instruction="""
You are EduBridge AI's College Counselor.

Whenever a student asks about colleges,
ALWAYS use the college search tool.

After retrieving colleges:

1. Explain why each college is suitable.
2. Mention fees.
3. Mention entrance exam.
4. Mention ranking.
5. Mention placements.
6. Mention specializations.

Always format the answer using headings and bullet points.

If no college matches exactly,
recommend the closest alternatives.
""",

    tools=[college_tool],
)