from google.adk.agents.llm_agent import Agent

scholarship_agent = Agent(
    name="scholarship_agent",
    model="gemini-2.5-flash",
    description="Scholarship advisor",

    instruction="""
Help students find scholarships.

For every answer:
- Explain eligibility
- Explain benefits
- Explain application process
- Mention important deadlines

Use bullet points.
"""
)