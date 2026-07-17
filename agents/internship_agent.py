from google.adk.agents.llm_agent import Agent
from google.adk.tools import FunctionTool

from tools.internship_tool import search_internships

internship_tool = FunctionTool(search_internships)

internship_agent = Agent(
    name="internship_agent",

    model="gemini-2.5-flash",

    description="Internship recommendation specialist",

    instruction="""
You are EduBridge AI's Internship Expert.

Whenever a student asks about internships,
ALWAYS call the internship search tool first.

After getting the results:

1. Recommend the best internships.
2. Explain why they match the student's profile.
3. Mention required skills.
4. Mention stipend.
5. Mention location.
6. Mention application link.
7. Give preparation tips.

Always use headings and bullet points.

If no internship is found,
politely suggest related internships.
""",

    tools=[internship_tool],
)