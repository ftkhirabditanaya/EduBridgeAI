from google.adk.agents.llm_agent import Agent

from .career_agent import career_agent
from .college_agent import college_agent
from .scholarship_agent import scholarship_agent
from .study_planner_agent import study_planner_agent
from .internship_agent import internship_agent
from .resume_agent import resume_agent
root_agent = Agent(
    name="edubridge_coordinator",
    model="gemini-2.5-flash",

    description="Educational guidance coordinator",

    instruction="""
You are EduBridge AI.

You coordinate multiple educational AI specialists.

Your responsibility is to understand the student's request and delegate it to the most appropriate specialist.

Available specialists include:

• Career Guidance
• College Recommendations
• Scholarships
• Study Planning
• Internship Guidance

Always choose the best specialist automatically.

If the student's request involves internships, skills, resume building, portfolio projects, interview preparation, GitHub improvement, or job readiness, delegate to the Internship Agent.

Do not answer specialist questions yourself unless necessary.
""",

    sub_agents=[
        career_agent,
        college_agent,
        scholarship_agent,
        study_planner_agent,
        internship_agent,
        resume_agent, 
    ]
)