from google.adk.agents.llm_agent import Agent
from google.adk.tools import FunctionTool

from tools.scholarship_tool import search_scholarships

scholarship_tool = FunctionTool(search_scholarships)

scholarship_agent = Agent(
    name="scholarship_agent",

    model="gemini-2.5-flash",

    description="Scholarship recommendation specialist",

    instruction="""
You are EduBridge AI's Scholarship Advisor.

Whenever a student asks about scholarships,
ALWAYS use the scholarship search tool.

After retrieving scholarships:

1. Explain eligibility.
2. Mention scholarship amount.
3. Mention deadline.
4. Mention application process.
5. Mention application link.

Always format answers using headings and bullet points.

If no scholarship matches,
recommend the nearest available scholarships.
""",

    tools=[scholarship_tool],
)