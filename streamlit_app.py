"""EduBridge AI — Streamlit education guidance frontend."""

import streamlit as st
import pandas as pd
import os
import time
import plotly.graph_objects as go
import plotly.express as px

from tools.pathway_planner_tool import create_pathway_plan

# ============================================
# Page Configuration
# ============================================

st.set_page_config(
    page_title="EduBridge AI — Your AI Education Guide",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================
# Load Custom CSS
# ============================================

def load_css():
    css_path = os.path.join(
        os.path.dirname(__file__), "assets", "styles.css"
    )
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Inject Google Fonts
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)


# ============================================
# Database Paths
# ============================================

BASE_DIR = os.path.dirname(__file__)
DB_DIR = os.path.join(BASE_DIR, "database")


def load_csv(filename):
    path = os.path.join(DB_DIR, filename)
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame()


# ============================================
# Helper: Render Score Gauge
# ============================================

def render_score_gauge(score, title="ATS Score"):
    if score >= 70:
        color = "#43835c"
    elif score >= 40:
        color = "#98792d"
    else:
        color = "#a64e4a"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": title, "font": {"family": "Space Grotesk", "size": 18, "color": "#526553"}},
        number={"font": {"family": "Space Grotesk", "size": 48, "color": "#456b4b"}},
        gauge={
            "axis": {"range": [0, 100], "tickwidth": 1, "tickcolor": "#82907d"},
            "bar": {"color": color, "thickness": 0.3},
            "bgcolor": "#e9eee3",
            "borderwidth": 2,
            "bordercolor": "#cbd8c3",
            "steps": [
                {"range": [0, 40], "color": "#f0dfda"},
                {"range": [40, 70], "color": "#f4ebcb"},
                {"range": [70, 100], "color": "#dce9dc"},
            ],
        }
    ))
    fig.update_layout(
        height=250,
        margin=dict(l=30, r=30, t=60, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        font={"family": "DM Sans", "color": "#526553"},
    )
    return fig


def style_chart(fig):
    fig.update_layout(
        font={"family": "DM Sans", "color": "#526553"},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis={
            "color": "#526553",
            "gridcolor": "#dfe7d8",
            "zerolinecolor": "#c6d3bf",
        },
        yaxis={
            "color": "#526553",
            "gridcolor": "#dfe7d8",
            "zerolinecolor": "#c6d3bf",
        },
    )
    return fig


# ============================================
# Helper: Render Feature Card HTML
# ============================================

def feature_card(title, desc):
    return f"""
    <div class="feature-card fade-in">
        <div class="feature-title">{title}</div>
        <div class="feature-desc">{desc}</div>
    </div>
    """


# ============================================
# Sidebar
# ============================================

with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <div class="brand-mark">E</div>
        <div class="brand-name">
            EduBridge AI
        </div>
        <div class="brand-caption">
            AI-Powered Education Guide
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    page = st.radio(
        "Navigate",
        [
            "Home",
            "AI Chat",
            "Pathway Planner",
            "Career Explorer",
            "College Finder",
            "Internship Hub",
            "Scholarships",
            "Resume Analyzer",
            "Project Ideas",
            "Skills Dashboard",
        ],
        label_visibility="collapsed",
    )

    st.markdown("---")

    st.markdown("""
    <div class="footer-text" style="border-top: none; margin-top: 1.5rem; padding-top: 0;">
        Created by <a href="https://github.com/ftkhirabditanaya" target="_blank">Khirabdi Tanaya</a>
    </div>
    """, unsafe_allow_html=True)


# ============================================
# PAGE: Home
# ============================================

if page == "Home":

    # Hero Section
    st.markdown("""
    <div class="hero-container fade-in">
        <div class="hero-title">EduBridge AI</div>
        <div class="hero-subtitle">
            Your intelligent companion for career guidance, college recommendations,
            scholarships, internships, and personalized study planning — all powered by
            Google Gemini AI.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Section divider
    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Feature Cards
    st.markdown("### What Can EduBridge AI Do For You?")
    st.markdown("<div class='section-divider' style='margin: 0.75rem 0 1.5rem 0;'></div>", unsafe_allow_html=True)

    row1_cols = st.columns(3)

    with row1_cols[0]:
        st.markdown(feature_card(
            "Career Guidance",
            "Get AI-powered career recommendations based on your stream, skills, and interests."
        ), unsafe_allow_html=True)

    with row1_cols[1]:
        st.markdown(feature_card(
            "College Finder",
            "Discover top colleges matching your course preferences with fees, rankings, and more."
        ), unsafe_allow_html=True)

    with row1_cols[2]:
        st.markdown(feature_card(
            "Scholarships",
            "Find scholarships you're eligible for with amounts, deadlines, and application details."
        ), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    row2_cols = st.columns(3)

    with row2_cols[0]:
        st.markdown(feature_card(
            "Internship Hub",
            "Search internships by domain, location, mode, and stipend with smart recommendations."
        ), unsafe_allow_html=True)

    with row2_cols[1]:
        st.markdown(feature_card(
            "Resume Analyzer",
            "Upload your resume and get ATS scores, skill analysis, and improvement suggestions."
        ), unsafe_allow_html=True)

    with row2_cols[2]:
        st.markdown(feature_card(
            "Project Mentor",
            "Get portfolio project ideas with step-by-step guides for internships and placements."
        ), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    row3_cols = st.columns(3)

    with row3_cols[0]:
        st.markdown(feature_card(
            "Study Planner",
            "Generate personalized study plans with daily schedules, weekly targets, and revision strategies."
        ), unsafe_allow_html=True)

    with row3_cols[1]:
        st.markdown(feature_card(
            "Interview Prep",
            "Prepare for technical and HR interviews with curated questions and expert tips."
        ), unsafe_allow_html=True)

    with row3_cols[2]:
        st.markdown(feature_card(
            "Skills Dashboard",
            "Explore in-demand skills across categories and plan your learning journey."
        ), unsafe_allow_html=True)

    # Agent Architecture
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Multi-Agent Architecture")
    st.markdown("<div class='section-divider' style='margin: 0.75rem 0 1.5rem 0;'></div>", unsafe_allow_html=True)

    agents = [
        "Coordinator", "Career", "College", "Scholarship", "Study Planner",
        "Internship", "Resume", "ATS Scorer", "Interview", "Project Mentor",
    ]

    badges_html = '<div style="display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center;">'
    for name in agents:
        badges_html += f'<div class="agent-badge">{name}</div>'
    badges_html += '</div>'
    st.markdown(badges_html, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer-text">
        EduBridge AI 2026 • Built by
        <a href="https://github.com/ftkhirabditanaya" target="_blank">Khirabdi Tanaya</a>
        • Powered by Google Gemini AI
    </div>
    """, unsafe_allow_html=True)


# ============================================
# PAGE: AI Chat
# ============================================

elif page == "AI Chat":

    st.markdown("""
    <div class="hero-container fade-in" style="padding: 1rem 0;">
        <div class="hero-title" style="font-size: 2rem;">AI Chat Assistant</div>
        <div class="hero-subtitle" style="font-size: 0.95rem;">
            Ask anything about careers, colleges, scholarships, internships, and more.
            The AI coordinator will route your question to the best specialist.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    # Initialize chat history
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [
            {
                "role": "assistant",
                "content": """**Welcome to EduBridge AI!**

I'm your AI-powered educational guide. I can help you with:

- **Career Guidance** — Discover career paths based on your interests
- **College Recommendations** — Find the best colleges for your goals
- **Scholarships** — Search for scholarships you're eligible for
- **Internships** — Find internships matching your skills
- **Resume Analysis** — Get your resume scored and improved
- **Study Planning** — Create personalized study plans
- **Interview Prep** — Prepare for technical and HR interviews
- **Project Ideas** — Get portfolio project suggestions

**Try asking:** _"I'm a PCB student interested in AI. What careers can I pursue?"_"""
            }
        ]

    # Display chat messages
    for msg in st.session_state.chat_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    if prompt := st.chat_input("Ask me anything about your educational journey..."):
        # Add user message
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner(""):
                st.markdown("""
                <div class="loading-dots">
                    <span></span><span></span><span></span>
                </div>
                """, unsafe_allow_html=True)
                time.sleep(0.5)

            # Try to use the ADK agent
            try:
                from google import genai
                from dotenv import load_dotenv
                load_dotenv()

                client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

                # Build context from chat history
                history_text = ""
                for m in st.session_state.chat_messages[-6:]:
                    role = "Student" if m["role"] == "user" else "EduBridge AI"
                    history_text += f"{role}: {m['content']}\n\n"

                system_prompt = """You are EduBridge AI, an intelligent educational guidance assistant.
You help students with career guidance, college recommendations, scholarships,
internships, study planning, resume analysis, interview preparation, and project ideas.

Always respond with well-formatted markdown using headings, bullet points, and tables.
Be warm, supportive, and thorough in your responses.
Do not use emojis.
If the student asks about careers, recommend 3-5 options with details.
If asked about colleges, include fees, rankings, and entrance exams.
If asked about internships, include company, role, stipend, and skills needed.
Always be encouraging and student-friendly."""

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=f"{system_prompt}\n\nConversation:\n{history_text}\nStudent: {prompt}\n\nEduBridge AI:"
                )

                reply = response.text

            except Exception as e:
                reply = f"""I appreciate your question! However, I'm currently unable to connect to the AI service.

**Your question:** {prompt}

**To get a full AI-powered response, please ensure:**
1. Your `GOOGLE_API_KEY` is set in the `.env` file
2. The `google-genai` package is installed
3. You have an active internet connection

In the meantime, feel free to explore the other sections using the sidebar!

_Error: {str(e)}_"""

            st.markdown(reply)
            st.session_state.chat_messages.append({"role": "assistant", "content": reply})

    # Quick Action Buttons
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### Quick Questions")

    qcols = st.columns(3)

    quick_questions = [
        "What career paths are good for a PCB student interested in AI?",
        "Suggest top colleges for B.Tech in CSE in India",
        "Find scholarships for engineering students",
    ]

    for i, q in enumerate(quick_questions):
        with qcols[i]:
            if st.button(f"{q[:45]}...", key=f"qq_{i}", use_container_width=True):
                st.session_state.chat_messages.append({"role": "user", "content": q})
                st.rerun()


# ============================================
# PAGE: Pathway Planner
# ============================================

elif page == "Pathway Planner":

    st.markdown("""
    <div class="hero-container fade-in" style="padding: 1rem 0;">
        <div class="hero-title" style="font-size: 2rem;">Pathway Planner</div>
        <div class="hero-subtitle" style="font-size: 0.95rem;">
            Turn a career goal, the skills you already have, and your real-world constraints
            into an explainable plan with milestones, projects, opportunities, and funding leads.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
    st.info(
        "Plans are grounded in EduBridge's local catalog data. They are starting points, "
        "not admissions, job, or funding guarantees."
    )

    career_data = load_csv("careers.csv")
    skill_data = load_csv("skills.csv")
    if career_data.empty or "career" not in career_data.columns:
        st.error("Career catalog is missing or invalid; the pathway planner cannot run.")
    else:
        careers = sorted(career_data["career"].dropna().astype(str).unique().tolist())
        catalog_skills = (
            skill_data["skill"].dropna().astype(str).tolist()
            if not skill_data.empty and "skill" in skill_data.columns else []
        )

        with st.form("pathway_planner_form"):
            st.markdown("### 1. Set your direction")
            goal = st.selectbox("Career goal", careers)
            education_stage = st.selectbox(
                "Current education stage",
                ["Secondary school", "Undergraduate", "Graduate", "Other"],
            )
            streams = ["Not specified"]
            if "stream" in career_data.columns:
                streams += sorted(
                    career_data["stream"].dropna().astype(str).unique().tolist()
                )
            stream = st.selectbox("Academic stream (optional)", streams)

            goal_row = career_data[career_data["career"].astype(str) == goal].iloc[0]
            required_skills = [
                skill.strip()
                for skill in str(goal_row.get("required_skills", "")).split(",")
                if skill.strip()
            ]
            skill_options = sorted(set(catalog_skills + required_skills), key=str.lower)
            current_skills = st.multiselect(
                "Skills you already have",
                skill_options,
                help="Select only skills you can currently use; gaps are derived from the career catalog.",
            )

            st.markdown("### 2. Add your constraints")
            left, middle, right = st.columns(3)
            with left:
                weekly_hours = st.slider(
                    "Study hours per week", min_value=1, max_value=40, value=6
                )
            with middle:
                monthly_budget = st.number_input(
                    "Learning budget per month (₹)",
                    min_value=0,
                    max_value=100000,
                    value=0,
                    step=500,
                )
            with right:
                months = st.slider("Planning horizon (months)", 1, 24, 6)
            location = st.text_input(
                "Preferred internship location (optional)",
                placeholder="e.g., Bengaluru or Remote",
            )
            submitted = st.form_submit_button(
                "Build my pathway", type="primary", use_container_width=True
            )

        if submitted:
            try:
                plan = create_pathway_plan(
                    goal=goal,
                    current_skills=current_skills,
                    education_stage=education_stage,
                    weekly_hours=weekly_hours,
                    monthly_budget=monthly_budget,
                    months=months,
                    stream=""if stream == "Not specified" else stream,
                    location=location.strip(),
                )
                st.session_state["pathway_plan"] = plan
            except (ValueError, FileNotFoundError) as error:
                st.error(f"Could not build the pathway: {error}")
                st.session_state.pop("pathway_plan", None)

        plan = st.session_state.get("pathway_plan")
        if plan:
            st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
            st.markdown(f"## Your path to {plan['goal']}")
            metrics = st.columns(3)
            metrics[0].metric("Catalog skill gaps", len(plan["skills"]["gaps"]))
            metrics[1].metric(
                "Estimated focused hours", plan["effort"]["estimated_hours"]
            )
            metrics[2].metric(
                "Minimum months at this pace",
                plan["effort"]["minimum_months_at_current_pace"],
            )

            if plan["effort"]["timeline_fits"]:
                st.success(
                    f"Your {plan['constraints']['months']}-month horizon provides "
                    f"{plan['effort']['available_hours']} study hours at "
                    f"{plan['constraints']['weekly_hours']} hours per week."
                )
            else:
                st.warning(
                    f"This timeline may be ambitious: the plan estimates "
                    f"{plan['effort']['estimated_hours']} focused hours, while your "
                    f"current schedule provides {plan['effort']['available_hours']}. "
                    f"Consider extending the horizon to about "
                    f"{plan['effort']['minimum_months_at_current_pace']} months or adding study time."
                )

            st.markdown("### Why this pathway")
            st.write(
                f"EduBridge's **{plan['career'].get('degree', 'listed degree')}** career "
                f"catalog entry requires: {', '.join(plan['skills']['required']) or 'no skills listed'}."
            )
            st.write(
                f"Already covered: {', '.join(plan['skills']['already_have']) or 'none selected'}. "
                f"Priority gaps: {', '.join(plan['skills']['gaps']) or 'none from the catalog'}."
            )
            st.caption(
                f"Profile used: {plan['constraints']['education_stage']}; "
                f"{plan['constraints']['weekly_hours']} study hours/week; "
                f"₹{plan['constraints']['monthly_budget']:,}/month; "
                f"{plan['constraints']['months']} months."
            )
            st.caption(f"Budget approach: {plan['budget_guidance']}")

            st.markdown("### Milestones")
            for index, milestone in enumerate(plan["milestones"], start=1):
                with st.container(border=True):
                    st.markdown(
                        f"**{index}. {milestone['title']}** · {milestone['timeframe']}"
                    )
                    st.write(milestone["action"])
                    st.caption(f"Deliverable: {milestone['deliverable']}")
                    st.caption(f"Why: {milestone['rationale']}")

            st.markdown("### Portfolio project")
            if plan["project"]:
                st.write(
                    f"**{plan['project']['name']}** · {plan['project']['domain']} · "
                    f"{plan['project']['difficulty']}"
                )
                st.write(
                    f"Skills it demonstrates: {', '.join(plan['project']['matched_skills']) or 'career-adjacent practice'}."
                )
                st.caption(plan["project"]["reason"])
            else:
                st.info("No project entries are currently available in the local catalog.")

            st.markdown("### Internship leads")
            if plan["internships"]:
                for opportunity in plan["internships"]:
                    with st.container(border=True):
                        stipend = opportunity["stipend"]
                        st.markdown(
                            f"**{opportunity['role']} — {opportunity['company']}** "
                            f"· {opportunity['location']}"
                        )
                        st.write(
                            f"Catalog skill overlap: {opportunity['match_score']}% "
                            f"({', '.join(opportunity['matched_skills']) or 'no direct overlap'}). "
                            f"Skills still to build: "
                            f"{', '.join(opportunity['skills_to_build']) or 'none listed'}."
                        )
                        if stipend != "":
                            st.caption(f"Catalog stipend: ₹{float(stipend):,.0f}")
                        if opportunity["apply_link"]:
                            st.link_button(
                                f"View {opportunity['company']} opportunity",
                                opportunity["apply_link"],
                            )
                        st.caption(f"Match reason: {opportunity['reason']}")
            else:
                st.info("No internship entries are currently available in the local catalog.")

            st.markdown("### Funding leads to verify")
            st.caption(
                "These are catalog-based leads, not confirmed eligibility. Check each provider's "
                "official rules and current application date before relying on an award."
            )
            if plan["funding"]:
                funding_table = pd.DataFrame([
                    {
                        "Program": item["name"],
                        "Amount (₹)": item["amount"],
                        "Listed eligibility": item["eligibility"],
                        "Catalog deadline": item["deadline"],
                        "Planner signal": item["fit"],
                        "Why shown": item["reason"],
                    }
                    for item in plan["funding"]
                ])
                st.dataframe(funding_table, use_container_width=True, hide_index=True)
            else:
                st.info("No funding entries are currently available in the local catalog.")

            st.markdown("### How recommendations are calculated")
            for explanation in plan["explanation"]:
                st.write(f"- {explanation}")

            markdown_lines = [
                f"# Pathway to {plan['goal']}",
                "",
                f"- Education stage: {plan['constraints']['education_stage']}",
                f"- Study time: {plan['constraints']['weekly_hours']} hours/week",
                f"- Learning budget: ₹{plan['constraints']['monthly_budget']:,}/month",
                f"- Budget approach: {plan['budget_guidance']}",
                f"- Planning horizon: {plan['constraints']['months']} months",
                f"- Estimated effort: {plan['effort']['estimated_hours']} hours",
                "",
                "## Skill gaps",
                *(
                    [f"- {skill}"for skill in plan["skills"]["gaps"]]
                    or ["- No catalog gaps identified"]
                ),
                "",
                "## Milestones",
            ]
            for milestone in plan["milestones"]:
                markdown_lines.extend([
                    f"### {milestone['title']} ({milestone['timeframe']})",
                    milestone["action"],
                    f"Deliverable: {milestone['deliverable']}",
                    f"Why: {milestone['rationale']}",
                    "",
                ])
            markdown_lines.extend([
                "## Funding leads (verify with providers)",
                *[
                    f"- {item['name']}: ₹{item['amount']:,}; {item['eligibility']}; "
                    f"listed deadline: {item['deadline']}; {item['fit']}."
                    for item in plan["funding"]
                ],
                "",
                "Recommendations are derived from EduBridge's local catalogs and are not guarantees.",
            ])
            st.download_button(
                "Download my roadmap",
                data="\n".join(markdown_lines),
                file_name="edubridge-pathway-roadmap.md",
                mime="text/markdown",
            )


# ============================================
# PAGE: Career Explorer
# ============================================

elif page == "Career Explorer":

    st.markdown("""
    <div class="hero-container fade-in" style="padding: 1rem 0;">
        <div class="hero-title" style="font-size: 2rem;">Career Explorer</div>
        <div class="hero-subtitle" style="font-size: 0.95rem;">
            Discover career paths tailored to your academic background and interests.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    df = load_csv("careers.csv")

    if not df.empty:
        # Filters
        col1, col2 = st.columns(2)

        with col1:
            streams = ["All"] + sorted(df["stream"].unique().tolist())
            selected_stream = st.selectbox("Filter by Stream", streams)

        with col2:
            search = st.text_input("Search careers or skills", placeholder="e.g., Python, AI, Biology")

        # Apply filters
        filtered = df.copy()

        if selected_stream != "All":
            filtered = filtered[
                filtered["stream"].str.contains(selected_stream, case=False, na=False)
            ]

        if search:
            filtered = filtered[
                filtered.apply(lambda row: search.lower() in str(row).lower(), axis=1)
            ]

        st.markdown(f"<br>", unsafe_allow_html=True)
        st.markdown(f"### Showing {len(filtered)} Career Paths")

        # Career cards
        for _, career in filtered.iterrows():
            salary = career.get("average_salary", 0)
            salary_lpa = f"₹{salary/100000:.1f} LPA" if salary else "N/A"

            skills_list = career.get("required_skills", "")
            tags_html = ""
            if skills_list:
                for skill in str(skills_list).split(","):
                    tags_html += f'<span class="tag">{skill.strip()}</span> '

            st.markdown(f"""
            <div class="result-card">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <h4 style="margin: 0 0 0.25rem 0;">{career.get('career', 'N/A')}</h4>
                        <p style="margin: 0 0 0.5rem 0; font-size: 0.85rem;">{career.get('description', '')}</p>
                    </div>
                    <div class="stat-badge">{salary_lpa}</div>
                </div>
                <div style="margin: 0.75rem 0;">
                    {tags_html}
                </div>
                <div style="display: flex; gap: 1.5rem; font-size: 0.82rem; color: #6b7b6c;">
                    <span>Stream: <strong style="color: #526553;">{career.get('stream', 'N/A')}</strong></span>
                    <span>Degree: <strong style="color: #526553;">{career.get('degree', 'N/A')}</strong></span>
                    <span>Scope: <strong style="color: #526553;">{career.get('future_scope', 'N/A')}</strong></span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Salary Chart
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### Salary Comparison")

        if "average_salary" in filtered.columns and "career" in filtered.columns:
            chart_df = filtered[["career", "average_salary"]].dropna()
            chart_df["salary_lpa"] = chart_df["average_salary"] / 100000

            fig = px.bar(
                chart_df.sort_values("salary_lpa", ascending=True),
                x="salary_lpa",
                y="career",
                orientation="h",
                labels={"salary_lpa": "Average Salary (LPA)", "career": ""},
                color="salary_lpa",
                color_continuous_scale=["#d5e4c9", "#8eaf80", "#527957"],
            )
            fig.update_layout(
                height=400,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font={"family": "DM Sans", "color": "#526553"},
                showlegend=False,
                coloraxis_showscale=False,
                xaxis={"gridcolor": "#dfe7d8"},
                yaxis={"gridcolor": "#dfe7d8"},
                margin=dict(l=10, r=10, t=20, b=10),
            )
            st.plotly_chart(style_chart(fig), use_container_width=True)

    else:
        st.info("Career database not found. Please ensure `database/careers.csv` exists.")


# ============================================
# PAGE: College Finder
# ============================================

elif page == "College Finder":

    st.markdown("""
    <div class="hero-container fade-in" style="padding: 1rem 0;">
        <div class="hero-title" style="font-size: 2rem;">College Finder</div>
        <div class="hero-subtitle" style="font-size: 0.95rem;">
            Find the best colleges for your preferred course, with fees, rankings, and entrance details.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    df = load_csv("colleges.csv")

    if not df.empty:
        # Filters
        col1, col2, col3 = st.columns(3)

        with col1:
            courses = ["All"] + sorted(df["course"].unique().tolist())
            selected_course = st.selectbox("Course", courses)

        with col2:
            states = ["All"] + sorted(df["state"].unique().tolist())
            selected_state = st.selectbox("State", states)

        with col3:
            search = st.text_input("Search", placeholder="College name...")

        # Apply filters
        filtered = df.copy()

        if selected_course != "All":
            filtered = filtered[
                filtered["course"].str.contains(selected_course, case=False, na=False)
            ]

        if selected_state != "All":
            filtered = filtered[filtered["state"] == selected_state]

        if search:
            filtered = filtered[
                filtered.apply(lambda row: search.lower() in str(row).lower(), axis=1)
            ]

        st.markdown(f"<br>", unsafe_allow_html=True)
        st.markdown(f"### Found {len(filtered)} Colleges")

        # College cards
        for _, college in filtered.iterrows():
            fees = college.get("fees", 0)
            fees_str = f"₹{fees:,.0f}"if fees else "N/A"
            ranking = college.get("ranking", "N/A")

            rank_color = "#43835c" if ranking and ranking <= 10 else "#98792d" if ranking and ranking <= 20 else "#8d9cb0"

            st.markdown(f"""
            <div class="result-card">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <h4 style="margin: 0 0 0.5rem 0;">{college.get('college', 'N/A')}</h4>
                        <div style="display: flex; gap: 1rem; flex-wrap: wrap; font-size: 0.85rem; color: #6b7b6c;">
                            <span>{college.get('city', '')}, {college.get('state', '')}</span>
                            <span>{college.get('course', 'N/A')}</span>
                            <span>{college.get('exam', 'N/A')}</span>
                        </div>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 1.4rem; color: {rank_color};">
                            #{ranking}
                        </div>
                        <div style="font-size: 0.75rem; color: #6b7b6c;">Ranking</div>
                    </div>
                </div>
                <div style="margin-top: 0.75rem; padding-top: 0.75rem; border-top: 1px solid #c6d3bf;">
                    <span class="stat-badge">Fees: {fees_str}/year</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Fees comparison chart
        if len(filtered) > 1 and "fees" in filtered.columns:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### Fees Comparison")

            chart_df = filtered[["college", "fees"]].dropna()
            chart_df["fees_k"] = chart_df["fees"] / 1000

            fig = px.bar(
                chart_df.sort_values("fees_k"),
                x="college",
                y="fees_k",
                labels={"fees_k": "Annual Fees (₹ thousands)", "college": ""},
                color="fees_k",
                color_continuous_scale=["#f5ecc4", "#e8d486", "#9a8140"],
            )
            fig.update_layout(
                height=350,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font={"family": "DM Sans", "color": "#526553"},
                showlegend=False,
                coloraxis_showscale=False,
                xaxis={"gridcolor": "#dfe7d8", "tickangle": -25},
                yaxis={"gridcolor": "#dfe7d8"},
                margin=dict(l=10, r=10, t=20, b=10),
            )
            st.plotly_chart(style_chart(fig), use_container_width=True)

    else:
        st.info("College database not found. Please ensure `database/colleges.csv` exists.")


# ============================================
# PAGE: Internship Hub
# ============================================

elif page == "Internship Hub":

    st.markdown("""
    <div class="hero-container fade-in" style="padding: 1rem 0;">
        <div class="hero-title" style="font-size: 2rem;">Internship Hub</div>
        <div class="hero-subtitle" style="font-size: 0.95rem;">
            Find internships that match your skills, domain, and preferences with smart recommendations.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    df = load_csv("internships.csv")

    if not df.empty:
        # Filters
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            domains = ["All"] + sorted(df["domain"].unique().tolist())
            selected_domain = st.selectbox("Domain", domains)

        with col2:
            locations = ["All"] + sorted(df["location"].unique().tolist())
            selected_location = st.selectbox("Location", locations)

        with col3:
            modes = ["All"] + sorted(df["mode"].unique().tolist())
            selected_mode = st.selectbox("Mode", modes)

        with col4:
            min_stipend = st.number_input("Min Stipend (₹)", min_value=0, value=0, step=5000)

        # Apply filters
        filtered = df.copy()

        if selected_domain != "All":
            filtered = filtered[filtered["domain"] == selected_domain]

        if selected_location != "All":
            filtered = filtered[
                filtered["location"].str.contains(selected_location, case=False, na=False)
            ]

        if selected_mode != "All":
            filtered = filtered[filtered["mode"] == selected_mode]

        if min_stipend > 0:
            filtered = filtered[filtered["stipend"] >= min_stipend]

        st.markdown(f"<br>", unsafe_allow_html=True)
        st.markdown(f"### Found {len(filtered)} Internships")

        # Internship cards
        for _, intern in filtered.iterrows():
            stipend = intern.get("stipend", 0)
            stipend_str = f"₹{stipend:,.0f}/month" if stipend else "Unpaid"

            skills_list = intern.get("skills", "")
            tags_html = ""
            if skills_list:
                for skill in str(skills_list).split(","):
                    tags_html += f'<span class="tag">{skill.strip()}</span> '

            mode_color = "#43835c" if intern.get("mode") == "Remote" else "#527957" if intern.get("mode") == "Hybrid" else "#98792d"

            st.markdown(f"""
            <div class="result-card">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <h4 style="margin: 0;">{intern.get('company', 'N/A')}</h4>
                        <p style="margin: 0.25rem 0 0.5rem; font-size: 0.92rem; color: #526553; font-weight: 500;">
                            {intern.get('role', 'N/A')}
                        </p>
                    </div>
                    <div style="text-align: right;">
                        <div class="stat-badge" style="margin-bottom: 0.5rem;">{stipend_str}</div>
                        <div style="display: inline-block; background: {mode_color}15; color: {mode_color}; border: 1px solid {mode_color}40; border-radius: 6px; padding: 0.15rem 0.6rem; font-size: 0.78rem; font-weight: 600;">
                            {intern.get('mode', 'N/A')}
                        </div>
                    </div>
                </div>
                <div style="margin: 0.75rem 0;">{tags_html}</div>
                <div style="display: flex; gap: 1.5rem; font-size: 0.82rem; color: #6b7b6c; flex-wrap: wrap;">
                    <span>{intern.get('location', 'N/A')}</span>
                    <span>{intern.get('domain', 'N/A')}</span>
                    <span>{intern.get('branch', 'All')}</span>
                    <a href="{intern.get('apply_link', '#')}" target="_blank" style="color: #34583d; font-weight: 600; text-decoration: none;">
                        Apply Now
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Stipend chart
        if len(filtered) > 1 and "stipend" in filtered.columns:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### Stipend Comparison")

            chart_df = filtered[["company", "role", "stipend"]].dropna()
            chart_df["label"] = chart_df["company"] + " - " + chart_df["role"]
            chart_df["stipend_k"] = chart_df["stipend"] / 1000

            fig = px.bar(
                chart_df.sort_values("stipend_k", ascending=True),
                x="stipend_k",
                y="label",
                orientation="h",
                labels={"stipend_k": "Monthly Stipend (₹ thousands)", "label": ""},
                color="stipend_k",
                color_continuous_scale=["#d5e4c9", "#8eaf80", "#527957"],
            )
            fig.update_layout(
                height=max(300, len(chart_df) * 45),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font={"family": "DM Sans", "color": "#526553"},
                showlegend=False,
                coloraxis_showscale=False,
                xaxis={"gridcolor": "#dfe7d8"},
                yaxis={"gridcolor": "#dfe7d8"},
                margin=dict(l=10, r=10, t=20, b=10),
            )
            st.plotly_chart(style_chart(fig), use_container_width=True)

    else:
        st.info("Internship database not found. Please ensure `database/internships.csv` exists.")


# ============================================
# PAGE: Scholarships
# ============================================

elif page == "Scholarships":

    st.markdown("""
    <div class="hero-container fade-in" style="padding: 1rem 0;">
        <div class="hero-title" style="font-size: 2rem;">Scholarships</div>
        <div class="hero-subtitle" style="font-size: 0.95rem;">
            Discover scholarships you're eligible for, with amounts, eligibility, and deadlines.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    df = load_csv("scholarships.csv")

    if not df.empty:
        # Search
        search = st.text_input("Search scholarships", placeholder="e.g., Engineering, Merit, SC/ST...")

        filtered = df.copy()
        if search:
            filtered = filtered[
                filtered.apply(lambda row: search.lower() in str(row).lower(), axis=1)
            ]

        st.markdown(f"<br>", unsafe_allow_html=True)
        st.markdown(f"### Found {len(filtered)} Scholarships")

        for _, sch in filtered.iterrows():
            amount = sch.get("amount", 0)
            amount_str = f"₹{amount:,.0f}"if amount else "N/A"

            st.markdown(f"""
            <div class="result-card">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <h4 style="margin: 0 0 0.5rem 0;">{sch.get('scholarship', 'N/A')}</h4>
                        <p style="margin: 0; font-size: 0.88rem;">
                            <strong style="color: #526553;">Eligibility:</strong>
                            {sch.get('eligibility', 'N/A')}
                        </p>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 1.3rem; color: #456b4b;">
                            {amount_str}
                        </div>
                        <div style="font-size: 0.75rem; color: #6b7b6c;">Scholarship Amount</div>
                    </div>
                </div>
                <div style="margin-top: 0.75rem; padding-top: 0.75rem; border-top: 1px solid #c6d3bf;">
                    <span style="font-size: 0.85rem; color: #6b7b6c;">
                        <strong>Deadline:</strong> {sch.get('last_date', 'N/A')}
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Amount comparison
        if len(filtered) > 1 and "amount" in filtered.columns:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### Scholarship Amount Comparison")

            chart_df = filtered[["scholarship", "amount"]].dropna()
            chart_df["amount_k"] = chart_df["amount"] / 1000

            fig = px.bar(
                chart_df.sort_values("amount_k", ascending=True),
                x="amount_k",
                y="scholarship",
                orientation="h",
                labels={"amount_k": "Amount (₹ thousands)", "scholarship": ""},
                color="amount_k",
                color_continuous_scale=["#f5ecc4", "#e8d486", "#9a8140"],
            )
            fig.update_layout(
                height=max(300, len(chart_df) * 45),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font={"family": "DM Sans", "color": "#526553"},
                showlegend=False,
                coloraxis_showscale=False,
                xaxis={"gridcolor": "#dfe7d8"},
                yaxis={"gridcolor": "#dfe7d8"},
                margin=dict(l=10, r=10, t=20, b=10),
            )
            st.plotly_chart(style_chart(fig), use_container_width=True)

    else:
        st.info("Scholarship database not found. Please ensure `database/scholarships.csv` exists.")


# ============================================
# PAGE: Resume Analyzer
# ============================================

elif page == "Resume Analyzer":

    st.markdown("""
    <div class="hero-container fade-in" style="padding: 1rem 0;">
        <div class="hero-title" style="font-size: 2rem;">Resume Analyzer</div>
        <div class="hero-subtitle" style="font-size: 0.95rem;">
            Upload your resume and get an ATS compatibility score, skill analysis,
            and personalized improvement suggestions.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Upload your resume (PDF, DOCX, or TXT)",
        type=["pdf", "docx", "txt"],
        help="We'll analyze your resume for ATS compatibility and skill gaps."
    )

    # Also allow pasting text
    with st.expander("Or paste your resume text"):
        pasted_text = st.text_area(
            "Paste resume text here",
            height=200,
            placeholder="Paste your resume content here..."
        )

    resume_text = None

    if uploaded_file is not None:
        # Save uploaded file
        upload_dir = os.path.join(BASE_DIR, "uploads")
        os.makedirs(upload_dir, exist_ok=True)
        file_path = os.path.join(upload_dir, uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Extract text
        try:
            from tools.resume_parser import extract_text
            resume_text = extract_text(file_path)
            st.success(f"Resume uploaded successfully: **{uploaded_file.name}**")
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")

    elif pasted_text and pasted_text.strip():
        resume_text = pasted_text.strip()

    if resume_text:
        st.markdown("<br>", unsafe_allow_html=True)

        with st.spinner("Analyzing your resume..."):
            time.sleep(0.5)

            # Analyze resume
            from tools.resume_analyzer import analyze_resume
            from tools.ats_scorer import calculate_ats_score

            analysis = analyze_resume(resume_text)
            ats = calculate_ats_score(resume_text)

        # Results in tabs
        tab1, tab2, tab3 = st.tabs(["ATS Score", "Analysis", "Recommendations"])

        with tab1:
            st.markdown("<br>", unsafe_allow_html=True)

            col1, col2 = st.columns([1, 1])

            with col1:
                # Score gauge
                fig = render_score_gauge(ats["ATS Score"])
                st.plotly_chart(style_chart(fig), use_container_width=True)

            with col2:
                st.markdown("#### Strengths")
                if ats.get("Strengths"):
                    for s in ats["Strengths"]:
                        st.markdown(s)
                else:
                    st.markdown("_No major strengths detected yet._")

                st.markdown("<br>", unsafe_allow_html=True)

                st.markdown("#### Suggestions")
                if ats.get("Suggestions"):
                    for s in ats["Suggestions"]:
                        st.markdown(s)
                else:
                    st.markdown("_Looking good! No additional suggestions._")

            # Skills breakdown
            st.markdown("<br>", unsafe_allow_html=True)

            scol1, scol2 = st.columns(2)

            with scol1:
                st.markdown("#### Technical Skills Found")
                if ats.get("Technical Skills"):
                    tags = " ".join([f'<span class="tag">{s.title()}</span>'for s in ats["Technical Skills"]])
                    st.markdown(f"<div>{tags}</div>", unsafe_allow_html=True)
                else:
                    st.info("No technical skills detected.")

            with scol2:
                st.markdown("#### Missing Skills")
                if ats.get("Missing Skills"):
                    tags = " ".join([f'<span class="tag" style="background: rgba(255,133,142,0.12); color: #a64e4a;">{s.title()}</span>'for s in ats["Missing Skills"][:8]])
                    st.markdown(f"<div>{tags}</div>", unsafe_allow_html=True)
                else:
                    st.success("Great! No critical missing skills.")

        with tab2:
            st.markdown("<br>", unsafe_allow_html=True)

            # Personal info
            info_col1, info_col2, info_col3 = st.columns(3)
            with info_col1:
                st.metric("Name", analysis.get("Name", "N/A"))
            with info_col2:
                st.metric("Email", analysis.get("Email", "N/A"))
            with info_col3:
                st.metric("Phone", analysis.get("Phone", "N/A"))

            st.markdown("<br>", unsafe_allow_html=True)

            # Skills, Education, Projects, Experience
            det_col1, det_col2 = st.columns(2)

            with det_col1:
                st.markdown("#### Skills Detected")
                if analysis.get("Skills"):
                    tags = " ".join([f'<span class="tag">{s}</span>'for s in analysis["Skills"]])
                    st.markdown(f"<div>{tags}</div>", unsafe_allow_html=True)
                else:
                    st.info("No skills detected.")

                st.markdown("<br>", unsafe_allow_html=True)

                st.markdown("#### Education")
                if analysis.get("Education"):
                    for edu in analysis["Education"]:
                        st.markdown(f"• {edu}")
                else:
                    st.info("No education details found.")

            with det_col2:
                st.markdown("#### Projects")
                if analysis.get("Projects"):
                    for proj in analysis["Projects"]:
                        st.markdown(f"• {proj}")
                else:
                    st.info("No projects detected.")

                st.markdown("<br>", unsafe_allow_html=True)

                st.markdown("#### Experience")
                if analysis.get("Experience"):
                    for exp in analysis["Experience"]:
                        st.markdown(f"• {exp}")
                else:
                    st.info("No experience entries found.")

        with tab3:
            st.markdown("<br>", unsafe_allow_html=True)

            # Internship matching
            st.markdown("#### Recommended Internships Based on Your Resume")

            try:
                from tools.recommendation_resume import recommend_from_resume, calculate_resume_score

                internships_df = load_csv("internships.csv")

                if not internships_df.empty:
                    recommendations = []
                    for _, intern in internships_df.iterrows():
                        result = calculate_resume_score(analysis, intern.to_dict())
                        recommendations.append(result)

                    recommendations.sort(key=lambda x: x["score"], reverse=True)

                    for rec in recommendations[:5]:
                        match_tags = " ".join([f'<span class="tag">{s}</span>'for s in rec.get("matched_skills", [])])
                        missing_tags = " ".join([f'<span class="tag" style="background: rgba(255,133,142,0.12); color: #a64e4a;">{s}</span>'for s in rec.get("missing_skills", [])])

                        st.markdown(f"""
                        <div class="result-card">
                            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                                <div>
                                    <h4 style="margin: 0;">{rec.get('company', 'N/A')}</h4>
                                    <p style="margin: 0.25rem 0; font-weight: 500; color: #526553;">{rec.get('role', 'N/A')}</p>
                                </div>
                                <div style="font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 1.5rem; color: {'#43835c' if rec['score'] >= 70 else '#98792d' if rec['score'] >= 40 else '#a64e4a'};">
                                    {rec['score']}%
                                </div>
                            </div>
                            <div style="margin-top: 0.5rem;">
                                <div style="font-size: 0.82rem; color: #6b7b6c; margin-bottom: 0.25rem;">Matched Skills:</div>
                                {match_tags if match_tags else '<span style="font-size: 0.82rem; color: #6b7b6c;">None</span>'}
                            </div>
                            <div style="margin-top: 0.5rem;">
                                <div style="font-size: 0.82rem; color: #6b7b6c; margin-bottom: 0.25rem;">Skills to Learn:</div>
                                {missing_tags if missing_tags else '<span style="font-size: 0.82rem; color: #43835c;">All matched!</span>'}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("Internship database not available for matching.")

            except Exception as e:
                st.warning(f"Could not generate internship recommendations: {str(e)}")

    else:
        # Show sample analysis prompt
        st.markdown("""
        <div class="info-card" style="text-align: center; margin-top: 2rem;">
            <h4>Upload Your Resume to Get Started</h4>
            <p>
                We'll analyze your resume for ATS compatibility, extract your skills,
                and match you with the best internship opportunities.
                <br><br>
                Supported formats: <strong>PDF</strong>, <strong>DOCX</strong>, <strong>TXT</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)


# ============================================
# PAGE: Project Ideas
# ============================================

elif page == "Project Ideas":

    st.markdown("""
    <div class="hero-container fade-in" style="padding: 1rem 0;">
        <div class="hero-title" style="font-size: 2rem;">Project Ideas</div>
        <div class="hero-subtitle" style="font-size: 0.95rem;">
            Explore portfolio-worthy project ideas to strengthen your resume and GitHub profile.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    df = load_csv("projects.csv")

    if not df.empty:
        # Filters
        col1, col2 = st.columns(2)

        with col1:
            domains = ["All"] + sorted(df["domain"].unique().tolist())
            selected_domain = st.selectbox("Domain", domains)

        with col2:
            difficulties = ["All"] + sorted(df["difficulty"].unique().tolist())
            selected_diff = st.selectbox("Difficulty", difficulties)

        # Apply filters
        filtered = df.copy()

        if selected_domain != "All":
            filtered = filtered[filtered["domain"] == selected_domain]

        if selected_diff != "All":
            filtered = filtered[filtered["difficulty"] == selected_diff]

        st.markdown(f"<br>", unsafe_allow_html=True)
        st.markdown(f"### {len(filtered)} Project Ideas")

        for _, proj in filtered.iterrows():
            diff = proj.get("difficulty", "N/A")
            diff_color = "#43835c" if diff == "Easy" else "#98792d" if diff == "Medium" else "#a64e4a"

            skills_list = proj.get("skills", "")
            tags_html = ""
            if skills_list:
                for skill in str(skills_list).split(","):
                    tags_html += f'<span class="tag">{skill.strip()}</span> '

            st.markdown(f"""
            <div class="result-card">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <h4 style="margin: 0 0 0.5rem 0;">{proj.get('project', 'N/A')}</h4>
                        <span style="font-size: 0.82rem; color: #6b7b6c;">{proj.get('domain', 'N/A')}</span>
                    </div>
                    <div style="display: inline-block; background: {diff_color}15; color: {diff_color}; border: 1px solid {diff_color}40; border-radius: 9999px; padding: 0.3rem 1rem; font-size: 0.82rem; font-weight: 700;">
                        {diff}
                    </div>
                </div>
                <div style="margin-top: 0.75rem;">
                    <div style="font-size: 0.82rem; color: #6b7b6c; margin-bottom: 0.25rem;">Required Skills:</div>
                    {tags_html}
                </div>
            </div>
            """, unsafe_allow_html=True)

    else:
        st.info("Project database not found. Please ensure `database/projects.csv` exists.")


# ============================================
# PAGE: Skills Dashboard
# ============================================

elif page == "Skills Dashboard":

    st.markdown("""
    <div class="hero-container fade-in" style="padding: 1rem 0;">
        <div class="hero-title" style="font-size: 2rem;">Skills Dashboard</div>
        <div class="hero-subtitle" style="font-size: 0.95rem;">
            Explore in-demand skills across categories and plan your learning journey.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    df = load_csv("skills.csv")

    if not df.empty:
        # Overview metrics
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Skills", str(len(df)))
        with col2:
            st.metric("Categories", str(df["category"].nunique()))
        with col3:
            easy_count = len(df[df["difficulty"] == "Easy"])
            st.metric("Beginner-Friendly", str(easy_count))

        st.markdown("<br>", unsafe_allow_html=True)

        # Skills by category
        st.markdown("### Skills by Category")

        categories = df["category"].unique()

        for cat in sorted(categories):
            cat_skills = df[df["category"] == cat]

            with st.expander(f"{cat} ({len(cat_skills)} skills)", expanded=False):
                for _, skill in cat_skills.iterrows():
                    diff = skill.get("difficulty", "N/A")
                    diff_color = "#43835c" if diff == "Easy" else "#98792d" if diff == "Medium" else "#a64e4a"

                    st.markdown(f"""
                    <div style="display: flex; justify-content: space-between; align-items: center;
                                padding: 0.6rem 0; border-bottom: 1px solid #c6d3bf;">
                        <span style="font-weight: 600; color: #526553; font-family: 'DM Sans', sans-serif;">
                            {skill.get('skill', 'N/A')}
                        </span>
                        <span style="display: inline-block; background: {diff_color}15; color: {diff_color};
                                     border-radius: 6px; padding: 0.15rem 0.6rem; font-size: 0.78rem; font-weight: 600;">
                            {diff}
                        </span>
                    </div>
                    """, unsafe_allow_html=True)

        # Distribution chart
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### Difficulty Distribution")

        diff_counts = df["difficulty"].value_counts()

        colors_map = {"Easy": "#43835c", "Medium": "#98792d", "Hard": "#a64e4a"}
        colors = [colors_map.get(d, "#6b7b6c") for d in diff_counts.index]

        fig = go.Figure(data=[go.Pie(
            labels=diff_counts.index,
            values=diff_counts.values,
            marker=dict(colors=colors, line=dict(color="#f8f6e9", width=3)),
            textinfo="label+percent",
            textfont=dict(family="DM Sans", size=14),
            hole=0.45,
        )])

        fig.update_layout(
            height=350,
            paper_bgcolor="rgba(0,0,0,0)",
            font={"family": "DM Sans", "color": "#526553"},
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5),
            margin=dict(l=20, r=20, t=20, b=40),
        )
        st.plotly_chart(style_chart(fig), use_container_width=True)

        # Category chart
        st.markdown("### Skills per Category")

        cat_counts = df["category"].value_counts()

        fig2 = px.bar(
            x=cat_counts.index,
            y=cat_counts.values,
            labels={"x": "Category", "y": "Number of Skills"},
            color=cat_counts.values,
            color_continuous_scale=["#d5e4c9", "#8eaf80", "#527957"],
        )
        fig2.update_layout(
            height=350,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font={"family": "DM Sans", "color": "#526553"},
            showlegend=False,
            coloraxis_showscale=False,
            xaxis={"gridcolor": "#dfe7d8"},
            yaxis={"gridcolor": "#dfe7d8"},
            margin=dict(l=10, r=10, t=20, b=10),
        )
        st.plotly_chart(style_chart(fig2), use_container_width=True)

    else:
        st.info("Skills database not found. Please ensure `database/skills.csv` exists.")
