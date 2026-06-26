from google.adk.agents.llm_agent import Agent

from .career_agent import career_agent
from .college_agent import college_agent
from .scholarship_agent import scholarship_agent
from .study_planner_agent import study_planner_agent

root_agent = Agent(
    name="edubridge_coordinator",
    model="gemini-2.5-flash",

    description="Educational guidance coordinator",

    instruction="""
You are EduBridge AI.

You help students with:
- Career guidance
- College recommendations
- Scholarships
- Study plans

Analyze the student's query and delegate it
to the most appropriate specialist agent.

Examples:
- Career questions → career_agent
- College questions → college_agent
- Scholarship questions → scholarship_agent
- Study planning questions → study_planner_agent

If multiple topics are involved, combine the
responses from relevant agents.
""",

    sub_agents=[
        career_agent,
        college_agent,
        scholarship_agent,
        study_planner_agent,
    ]
)