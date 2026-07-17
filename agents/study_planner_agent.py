from google.adk.agents.llm_agent import Agent

study_planner_agent = Agent(
    name="study_planner_agent",
    model="gemini-2.5-flash",
    description="Study planning specialist",

    instruction="""
Create realistic study plans.

Include:
- Daily schedule
- Weekly targets
- Revision plan
- Practice strategy

Keep plans practical.
"""
)