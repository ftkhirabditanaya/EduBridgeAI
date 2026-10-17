"""
EduBridge AI — Streamlit Frontend
Light Blue Pastel & Cream Theme
"""

import streamlit as st
import pandas as pd
import os
import time
import plotly.graph_objects as go
import plotly.express as px

# ============================================
# Page Configuration
# ============================================

st.set_page_config(
    page_title="EduBridge AI — Your AI Education Guide",
    page_icon="🎓",
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
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Inject Google Fonts
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
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
        color = "#34d399"
    elif score >= 40:
        color = "#fbbf24"
    else:
        color = "#f87171"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": title, "font": {"family": "Outfit", "size": 18, "color": "#374151"}},
        number={"font": {"family": "Outfit", "size": 48, "color": "#265ea3"}},
        gauge={
            "axis": {"range": [0, 100], "tickwidth": 1, "tickcolor": "#b8daff"},
            "bar": {"color": color, "thickness": 0.3},
            "bgcolor": "#f0f7ff",
            "borderwidth": 2,
            "bordercolor": "#b8daff",
            "steps": [
                {"range": [0, 40], "color": "#fef2f2"},
                {"range": [40, 70], "color": "#fefce8"},
                {"range": [70, 100], "color": "#ecfdf5"},
            ],
        }
    ))
    fig.update_layout(
        height=250,
        margin=dict(l=30, r=30, t=60, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        font={"family": "Inter"},
    )
    return fig


# ============================================
# Helper: Render Feature Card HTML
# ============================================

def feature_card(icon, title, desc):
    return f"""
    <div class="feature-card fade-in">
        <span class="feature-icon">{icon}</span>
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
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🎓</div>
        <div style="font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 1.4rem; color: #265ea3; letter-spacing: -0.02em;">
            EduBridge AI
        </div>
        <div style="font-family: 'Inter', sans-serif; font-size: 0.78rem; color: #9aa0ae; margin-top: 0.25rem;">
            AI-Powered Education Guide
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    page = st.radio(
        "Navigate",
        [
            "🏠  Home",
            "💬  AI Chat",
            "🧭  Career Explorer",
            "🏫  College Finder",
            "🎯  Internship Hub",
            "🏆  Scholarships",
            "📄  Resume Analyzer",
            "💡  Project Ideas",
            "📊  Skills Dashboard",
        ],
        label_visibility="collapsed",
    )

    st.markdown("---")

    st.markdown("""
    <div style="padding: 0.75rem; background: linear-gradient(135deg, rgba(224,239,255,0.5), rgba(254,249,238,0.5)); border-radius: 12px; border: 1px solid #b8daff;">
        <div style="font-family: 'Inter', sans-serif; font-size: 0.78rem; color: #6b7280; line-height: 1.6;">
            <span class="live-dot"></span> <strong style="color: #265ea3;">Powered by</strong><br>
            Google Gemini 2.5 Flash<br>
            Google Agent Development Kit
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer-text" style="border-top: none; margin-top: 1.5rem; padding-top: 0;">
        Made with ❤️ by <a href="https://github.com/ftkhirabditanaya" target="_blank">Khirabdi Tanaya</a>
    </div>
    """, unsafe_allow_html=True)


# ============================================
# PAGE: Home
# ============================================

if page == "🏠  Home":

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

    # Stats Row
    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🤖 AI Agents", "9")
    with col2:
        careers_df = load_csv("careers.csv")
        st.metric("🧭 Careers", str(len(careers_df)))
    with col3:
        internships_df = load_csv("internships.csv")
        st.metric("🎯 Internships", str(len(internships_df)))
    with col4:
        scholarships_df = load_csv("scholarships.csv")
        st.metric("🏆 Scholarships", str(len(scholarships_df)))

    st.markdown("<br>", unsafe_allow_html=True)

    # Feature Cards
    st.markdown("### ✨ What Can EduBridge AI Do For You?")
    st.markdown("<div class='section-divider' style='margin: 0.75rem 0 1.5rem 0;'></div>", unsafe_allow_html=True)

    row1_cols = st.columns(3)

    with row1_cols[0]:
        st.markdown(feature_card(
            "🧭", "Career Guidance",
            "Get AI-powered career recommendations based on your stream, skills, and interests."
        ), unsafe_allow_html=True)

    with row1_cols[1]:
        st.markdown(feature_card(
            "🏫", "College Finder",
            "Discover top colleges matching your course preferences with fees, rankings, and more."
        ), unsafe_allow_html=True)

    with row1_cols[2]:
        st.markdown(feature_card(
            "🏆", "Scholarships",
            "Find scholarships you're eligible for with amounts, deadlines, and application details."
        ), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    row2_cols = st.columns(3)

    with row2_cols[0]:
        st.markdown(feature_card(
            "🎯", "Internship Hub",
            "Search internships by domain, location, mode, and stipend with smart recommendations."
        ), unsafe_allow_html=True)

    with row2_cols[1]:
        st.markdown(feature_card(
            "📄", "Resume Analyzer",
            "Upload your resume and get ATS scores, skill analysis, and improvement suggestions."
        ), unsafe_allow_html=True)

    with row2_cols[2]:
        st.markdown(feature_card(
            "💡", "Project Mentor",
            "Get portfolio project ideas with step-by-step guides for internships and placements."
        ), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    row3_cols = st.columns(3)

    with row3_cols[0]:
        st.markdown(feature_card(
            "📚", "Study Planner",
            "Generate personalized study plans with daily schedules, weekly targets, and revision strategies."
        ), unsafe_allow_html=True)

    with row3_cols[1]:
        st.markdown(feature_card(
            "🎤", "Interview Prep",
            "Prepare for technical and HR interviews with curated questions and expert tips."
        ), unsafe_allow_html=True)

    with row3_cols[2]:
        st.markdown(feature_card(
            "📊", "Skills Dashboard",
            "Explore in-demand skills across categories and plan your learning journey."
        ), unsafe_allow_html=True)

    # Agent Architecture
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🏗️ Multi-Agent Architecture")
    st.markdown("<div class='section-divider' style='margin: 0.75rem 0 1.5rem 0;'></div>", unsafe_allow_html=True)

    agents = [
        ("🧠", "Coordinator"), ("🧭", "Career"), ("🏫", "College"),
        ("🏆", "Scholarship"), ("📚", "Study Planner"), ("🎯", "Internship"),
        ("📄", "Resume"), ("📊", "ATS Scorer"), ("🎤", "Interview"), ("💡", "Project Mentor"),
    ]

    badges_html = '<div style="display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center;">'
    for icon, name in agents:
        badges_html += f'<div class="agent-badge">{icon} {name}</div>'
    badges_html += '</div>'
    st.markdown(badges_html, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card" style="margin-top: 1.5rem; text-align: center;">
        <p style="margin: 0;">
            Built with <strong>Google Agent Development Kit (ADK)</strong> and
            <strong>Gemini 2.5 Flash</strong> — the coordinator automatically
            routes your questions to the right specialist agent.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer-text">
        EduBridge AI © 2026 • Built by
        <a href="https://github.com/ftkhirabditanaya" target="_blank">Khirabdi Tanaya</a>
        • Powered by Google Gemini AI
    </div>
    """, unsafe_allow_html=True)


# ============================================
# PAGE: AI Chat
# ============================================

elif page == "💬  AI Chat":

    st.markdown("""
    <div class="hero-container fade-in" style="padding: 1rem 0;">
        <div class="hero-title" style="font-size: 2rem;">💬 AI Chat Assistant</div>
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
                "content": """👋 **Welcome to EduBridge AI!**

I'm your AI-powered educational guide. I can help you with:

- 🧭 **Career Guidance** — Discover career paths based on your interests
- 🏫 **College Recommendations** — Find the best colleges for your goals
- 🏆 **Scholarships** — Search for scholarships you're eligible for
- 🎯 **Internships** — Find internships matching your skills
- 📄 **Resume Analysis** — Get your resume scored and improved
- 📚 **Study Planning** — Create personalized study plans
- 🎤 **Interview Prep** — Prepare for technical and HR interviews
- 💡 **Project Ideas** — Get portfolio project suggestions

**Try asking:** _"I'm a PCB student interested in AI. What careers can I pursue?"_"""
            }
        ]

    # Display chat messages
    for msg in st.session_state.chat_messages:
        with st.chat_message(msg["role"], avatar="🎓" if msg["role"] == "assistant" else "👤"):
            st.markdown(msg["content"])

    # Chat input
    if prompt := st.chat_input("Ask me anything about your educational journey..."):
        # Add user message
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("assistant", avatar="🎓"):
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

In the meantime, feel free to explore the other sections using the sidebar! 🎓

_Error: {str(e)}_"""

            st.markdown(reply)
            st.session_state.chat_messages.append({"role": "assistant", "content": reply})

    # Quick Action Buttons
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### 💡 Quick Questions")

    qcols = st.columns(3)

    quick_questions = [
        "What career paths are good for a PCB student interested in AI?",
        "Suggest top colleges for B.Tech in CSE in India",
        "Find scholarships for engineering students",
    ]

    for i, q in enumerate(quick_questions):
        with qcols[i]:
            if st.button(f"💬 {q[:45]}...", key=f"qq_{i}", use_container_width=True):
                st.session_state.chat_messages.append({"role": "user", "content": q})
                st.rerun()


# ============================================
# PAGE: Career Explorer
# ============================================

elif page == "🧭  Career Explorer":

    st.markdown("""
    <div class="hero-container fade-in" style="padding: 1rem 0;">
        <div class="hero-title" style="font-size: 2rem;">🧭 Career Explorer</div>
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
            selected_stream = st.selectbox("🎓 Filter by Stream", streams)

        with col2:
            search = st.text_input("🔍 Search careers or skills", placeholder="e.g., Python, AI, Biology")

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
                <div style="display: flex; gap: 1.5rem; font-size: 0.82rem; color: #9aa0ae;">
                    <span>📋 Stream: <strong style="color: #374151;">{career.get('stream', 'N/A')}</strong></span>
                    <span>🎓 Degree: <strong style="color: #374151;">{career.get('degree', 'N/A')}</strong></span>
                    <span>📈 Scope: <strong style="color: #374151;">{career.get('future_scope', 'N/A')}</strong></span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Salary Chart
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 📊 Salary Comparison")

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
                color_continuous_scale=["#b8daff", "#4a94e8", "#265ea3"],
            )
            fig.update_layout(
                height=400,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font={"family": "Inter", "color": "#374151"},
                showlegend=False,
                coloraxis_showscale=False,
                xaxis={"gridcolor": "#e0efff"},
                yaxis={"gridcolor": "#e0efff"},
                margin=dict(l=10, r=10, t=20, b=10),
            )
            st.plotly_chart(fig, use_container_width=True)

    else:
        st.info("Career database not found. Please ensure `database/careers.csv` exists.")


# ============================================
# PAGE: College Finder
# ============================================

elif page == "🏫  College Finder":

    st.markdown("""
    <div class="hero-container fade-in" style="padding: 1rem 0;">
        <div class="hero-title" style="font-size: 2rem;">🏫 College Finder</div>
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
            selected_course = st.selectbox("📖 Course", courses)

        with col2:
            states = ["All"] + sorted(df["state"].unique().tolist())
            selected_state = st.selectbox("📍 State", states)

        with col3:
            search = st.text_input("🔍 Search", placeholder="College name...")

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
        st.markdown(f"### 🏫 Found {len(filtered)} Colleges")

        # College cards
        for _, college in filtered.iterrows():
            fees = college.get("fees", 0)
            fees_str = f"₹{fees:,.0f}" if fees else "N/A"
            ranking = college.get("ranking", "N/A")

            rank_color = "#34d399" if ranking and ranking <= 10 else "#fbbf24" if ranking and ranking <= 20 else "#6b7280"

            st.markdown(f"""
            <div class="result-card">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <h4 style="margin: 0 0 0.5rem 0;">{college.get('college', 'N/A')}</h4>
                        <div style="display: flex; gap: 1rem; flex-wrap: wrap; font-size: 0.85rem; color: #6b7280;">
                            <span>📍 {college.get('city', '')}, {college.get('state', '')}</span>
                            <span>📖 {college.get('course', 'N/A')}</span>
                            <span>📝 {college.get('exam', 'N/A')}</span>
                        </div>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 1.4rem; color: {rank_color};">
                            #{ranking}
                        </div>
                        <div style="font-size: 0.75rem; color: #9aa0ae;">Ranking</div>
                    </div>
                </div>
                <div style="margin-top: 0.75rem; padding-top: 0.75rem; border-top: 1px solid #e0efff;">
                    <span class="stat-badge">💰 Fees: {fees_str}/year</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Fees comparison chart
        if len(filtered) > 1 and "fees" in filtered.columns:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### 📊 Fees Comparison")

            chart_df = filtered[["college", "fees"]].dropna()
            chart_df["fees_k"] = chart_df["fees"] / 1000

            fig = px.bar(
                chart_df.sort_values("fees_k"),
                x="college",
                y="fees_k",
                labels={"fees_k": "Annual Fees (₹ thousands)", "college": ""},
                color="fees_k",
                color_continuous_scale=["#fcecc8", "#f8dfa5", "#fbbf24"],
            )
            fig.update_layout(
                height=350,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font={"family": "Inter", "color": "#374151"},
                showlegend=False,
                coloraxis_showscale=False,
                xaxis={"gridcolor": "#e0efff", "tickangle": -25},
                yaxis={"gridcolor": "#e0efff"},
                margin=dict(l=10, r=10, t=20, b=10),
            )
            st.plotly_chart(fig, use_container_width=True)

    else:
        st.info("College database not found. Please ensure `database/colleges.csv` exists.")


# ============================================
# PAGE: Internship Hub
# ============================================

elif page == "🎯  Internship Hub":

    st.markdown("""
    <div class="hero-container fade-in" style="padding: 1rem 0;">
        <div class="hero-title" style="font-size: 2rem;">🎯 Internship Hub</div>
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
            selected_domain = st.selectbox("🔬 Domain", domains)

        with col2:
            locations = ["All"] + sorted(df["location"].unique().tolist())
            selected_location = st.selectbox("📍 Location", locations)

        with col3:
            modes = ["All"] + sorted(df["mode"].unique().tolist())
            selected_mode = st.selectbox("🏢 Mode", modes)

        with col4:
            min_stipend = st.number_input("💰 Min Stipend (₹)", min_value=0, value=0, step=5000)

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
        st.markdown(f"### 🎯 Found {len(filtered)} Internships")

        # Internship cards
        for _, intern in filtered.iterrows():
            stipend = intern.get("stipend", 0)
            stipend_str = f"₹{stipend:,.0f}/month" if stipend else "Unpaid"

            skills_list = intern.get("skills", "")
            tags_html = ""
            if skills_list:
                for skill in str(skills_list).split(","):
                    tags_html += f'<span class="tag">{skill.strip()}</span> '

            mode_color = "#34d399" if intern.get("mode") == "Remote" else "#60a5fa" if intern.get("mode") == "Hybrid" else "#fbbf24"

            st.markdown(f"""
            <div class="result-card">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <h4 style="margin: 0;">{intern.get('company', 'N/A')}</h4>
                        <p style="margin: 0.25rem 0 0.5rem; font-size: 0.92rem; color: #374151; font-weight: 500;">
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
                <div style="display: flex; gap: 1.5rem; font-size: 0.82rem; color: #9aa0ae; flex-wrap: wrap;">
                    <span>📍 {intern.get('location', 'N/A')}</span>
                    <span>🔬 {intern.get('domain', 'N/A')}</span>
                    <span>🎓 {intern.get('branch', 'All')}</span>
                    <a href="{intern.get('apply_link', '#')}" target="_blank" style="color: #4a94e8; font-weight: 600; text-decoration: none;">
                        🔗 Apply Now →
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Stipend chart
        if len(filtered) > 1 and "stipend" in filtered.columns:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### 📊 Stipend Comparison")

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
                color_continuous_scale=["#b8daff", "#4a94e8", "#265ea3"],
            )
            fig.update_layout(
                height=max(300, len(chart_df) * 45),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font={"family": "Inter", "color": "#374151"},
                showlegend=False,
                coloraxis_showscale=False,
                xaxis={"gridcolor": "#e0efff"},
                yaxis={"gridcolor": "#e0efff"},
                margin=dict(l=10, r=10, t=20, b=10),
            )
            st.plotly_chart(fig, use_container_width=True)

    else:
        st.info("Internship database not found. Please ensure `database/internships.csv` exists.")


# ============================================
# PAGE: Scholarships
# ============================================

elif page == "🏆  Scholarships":

    st.markdown("""
    <div class="hero-container fade-in" style="padding: 1rem 0;">
        <div class="hero-title" style="font-size: 2rem;">🏆 Scholarships</div>
        <div class="hero-subtitle" style="font-size: 0.95rem;">
            Discover scholarships you're eligible for, with amounts, eligibility, and deadlines.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    df = load_csv("scholarships.csv")

    if not df.empty:
        # Search
        search = st.text_input("🔍 Search scholarships", placeholder="e.g., Engineering, Merit, SC/ST...")

        filtered = df.copy()
        if search:
            filtered = filtered[
                filtered.apply(lambda row: search.lower() in str(row).lower(), axis=1)
            ]

        st.markdown(f"<br>", unsafe_allow_html=True)
        st.markdown(f"### 🏆 Found {len(filtered)} Scholarships")

        for _, sch in filtered.iterrows():
            amount = sch.get("amount", 0)
            amount_str = f"₹{amount:,.0f}" if amount else "N/A"

            st.markdown(f"""
            <div class="result-card">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <h4 style="margin: 0 0 0.5rem 0;">{sch.get('scholarship', 'N/A')}</h4>
                        <p style="margin: 0; font-size: 0.88rem;">
                            <strong style="color: #374151;">Eligibility:</strong>
                            {sch.get('eligibility', 'N/A')}
                        </p>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 1.3rem; color: #265ea3;">
                            {amount_str}
                        </div>
                        <div style="font-size: 0.75rem; color: #9aa0ae;">Scholarship Amount</div>
                    </div>
                </div>
                <div style="margin-top: 0.75rem; padding-top: 0.75rem; border-top: 1px solid #e0efff;">
                    <span style="font-size: 0.85rem; color: #6b7280;">
                        📅 <strong>Deadline:</strong> {sch.get('last_date', 'N/A')}
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Amount comparison
        if len(filtered) > 1 and "amount" in filtered.columns:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### 📊 Scholarship Amount Comparison")

            chart_df = filtered[["scholarship", "amount"]].dropna()
            chart_df["amount_k"] = chart_df["amount"] / 1000

            fig = px.bar(
                chart_df.sort_values("amount_k", ascending=True),
                x="amount_k",
                y="scholarship",
                orientation="h",
                labels={"amount_k": "Amount (₹ thousands)", "scholarship": ""},
                color="amount_k",
                color_continuous_scale=["#fcecc8", "#fbbf24", "#f59e0b"],
            )
            fig.update_layout(
                height=max(300, len(chart_df) * 45),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font={"family": "Inter", "color": "#374151"},
                showlegend=False,
                coloraxis_showscale=False,
                xaxis={"gridcolor": "#e0efff"},
                yaxis={"gridcolor": "#e0efff"},
                margin=dict(l=10, r=10, t=20, b=10),
            )
            st.plotly_chart(fig, use_container_width=True)

    else:
        st.info("Scholarship database not found. Please ensure `database/scholarships.csv` exists.")


# ============================================
# PAGE: Resume Analyzer
# ============================================

elif page == "📄  Resume Analyzer":

    st.markdown("""
    <div class="hero-container fade-in" style="padding: 1rem 0;">
        <div class="hero-title" style="font-size: 2rem;">📄 Resume Analyzer</div>
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
    with st.expander("📝 Or paste your resume text"):
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
            st.success(f"✅ Resume uploaded successfully: **{uploaded_file.name}**")
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")

    elif pasted_text and pasted_text.strip():
        resume_text = pasted_text.strip()

    if resume_text:
        st.markdown("<br>", unsafe_allow_html=True)

        with st.spinner("🔍 Analyzing your resume..."):
            time.sleep(0.5)

            # Analyze resume
            from tools.resume_analyzer import analyze_resume
            from tools.ats_scorer import calculate_ats_score

            analysis = analyze_resume(resume_text)
            ats = calculate_ats_score(resume_text)

        # Results in tabs
        tab1, tab2, tab3 = st.tabs(["📊 ATS Score", "🔍 Analysis", "💡 Recommendations"])

        with tab1:
            st.markdown("<br>", unsafe_allow_html=True)

            col1, col2 = st.columns([1, 1])

            with col1:
                # Score gauge
                fig = render_score_gauge(ats["ATS Score"])
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                st.markdown("#### Strengths")
                if ats.get("Strengths"):
                    for s in ats["Strengths"]:
                        st.markdown(f"✅ {s}")
                else:
                    st.markdown("_No major strengths detected yet._")

                st.markdown("<br>", unsafe_allow_html=True)

                st.markdown("#### Suggestions")
                if ats.get("Suggestions"):
                    for s in ats["Suggestions"]:
                        st.markdown(f"💡 {s}")
                else:
                    st.markdown("_Looking good! No additional suggestions._")

            # Skills breakdown
            st.markdown("<br>", unsafe_allow_html=True)

            scol1, scol2 = st.columns(2)

            with scol1:
                st.markdown("#### ✅ Technical Skills Found")
                if ats.get("Technical Skills"):
                    tags = " ".join([f'<span class="tag">{s.title()}</span>' for s in ats["Technical Skills"]])
                    st.markdown(f"<div>{tags}</div>", unsafe_allow_html=True)
                else:
                    st.info("No technical skills detected.")

            with scol2:
                st.markdown("#### ⚠️ Missing Skills")
                if ats.get("Missing Skills"):
                    tags = " ".join([f'<span class="tag" style="background: #fef2f2; color: #f87171;">{s.title()}</span>' for s in ats["Missing Skills"][:8]])
                    st.markdown(f"<div>{tags}</div>", unsafe_allow_html=True)
                else:
                    st.success("Great! No critical missing skills.")

        with tab2:
            st.markdown("<br>", unsafe_allow_html=True)

            # Personal info
            info_col1, info_col2, info_col3 = st.columns(3)
            with info_col1:
                st.metric("👤 Name", analysis.get("Name", "N/A"))
            with info_col2:
                st.metric("📧 Email", analysis.get("Email", "N/A"))
            with info_col3:
                st.metric("📱 Phone", analysis.get("Phone", "N/A"))

            st.markdown("<br>", unsafe_allow_html=True)

            # Skills, Education, Projects, Experience
            det_col1, det_col2 = st.columns(2)

            with det_col1:
                st.markdown("#### 🛠️ Skills Detected")
                if analysis.get("Skills"):
                    tags = " ".join([f'<span class="tag">{s}</span>' for s in analysis["Skills"]])
                    st.markdown(f"<div>{tags}</div>", unsafe_allow_html=True)
                else:
                    st.info("No skills detected.")

                st.markdown("<br>", unsafe_allow_html=True)

                st.markdown("#### 🎓 Education")
                if analysis.get("Education"):
                    for edu in analysis["Education"]:
                        st.markdown(f"• {edu}")
                else:
                    st.info("No education details found.")

            with det_col2:
                st.markdown("#### 💼 Projects")
                if analysis.get("Projects"):
                    for proj in analysis["Projects"]:
                        st.markdown(f"• {proj}")
                else:
                    st.info("No projects detected.")

                st.markdown("<br>", unsafe_allow_html=True)

                st.markdown("#### 🏢 Experience")
                if analysis.get("Experience"):
                    for exp in analysis["Experience"]:
                        st.markdown(f"• {exp}")
                else:
                    st.info("No experience entries found.")

        with tab3:
            st.markdown("<br>", unsafe_allow_html=True)

            # Internship matching
            st.markdown("#### 🎯 Recommended Internships Based on Your Resume")

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
                        match_tags = " ".join([f'<span class="tag">{s}</span>' for s in rec.get("matched_skills", [])])
                        missing_tags = " ".join([f'<span class="tag" style="background: #fef2f2; color: #f87171;">{s}</span>' for s in rec.get("missing_skills", [])])

                        st.markdown(f"""
                        <div class="result-card">
                            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                                <div>
                                    <h4 style="margin: 0;">{rec.get('company', 'N/A')}</h4>
                                    <p style="margin: 0.25rem 0; font-weight: 500; color: #374151;">{rec.get('role', 'N/A')}</p>
                                </div>
                                <div style="font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 1.5rem; color: {'#34d399' if rec['score'] >= 70 else '#fbbf24' if rec['score'] >= 40 else '#f87171'};">
                                    {rec['score']}%
                                </div>
                            </div>
                            <div style="margin-top: 0.5rem;">
                                <div style="font-size: 0.82rem; color: #9aa0ae; margin-bottom: 0.25rem;">Matched Skills:</div>
                                {match_tags if match_tags else '<span style="font-size: 0.82rem; color: #9aa0ae;">None</span>'}
                            </div>
                            <div style="margin-top: 0.5rem;">
                                <div style="font-size: 0.82rem; color: #9aa0ae; margin-bottom: 0.25rem;">Skills to Learn:</div>
                                {missing_tags if missing_tags else '<span style="font-size: 0.82rem; color: #34d399;">All matched!</span>'}
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
            <h4>📤 Upload Your Resume to Get Started</h4>
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

elif page == "💡  Project Ideas":

    st.markdown("""
    <div class="hero-container fade-in" style="padding: 1rem 0;">
        <div class="hero-title" style="font-size: 2rem;">💡 Project Ideas</div>
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
            selected_domain = st.selectbox("🔬 Domain", domains)

        with col2:
            difficulties = ["All"] + sorted(df["difficulty"].unique().tolist())
            selected_diff = st.selectbox("📊 Difficulty", difficulties)

        # Apply filters
        filtered = df.copy()

        if selected_domain != "All":
            filtered = filtered[filtered["domain"] == selected_domain]

        if selected_diff != "All":
            filtered = filtered[filtered["difficulty"] == selected_diff]

        st.markdown(f"<br>", unsafe_allow_html=True)
        st.markdown(f"### 💡 {len(filtered)} Project Ideas")

        for _, proj in filtered.iterrows():
            diff = proj.get("difficulty", "N/A")
            diff_color = "#34d399" if diff == "Easy" else "#fbbf24" if diff == "Medium" else "#f87171"

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
                        <span style="font-size: 0.82rem; color: #9aa0ae;">🔬 {proj.get('domain', 'N/A')}</span>
                    </div>
                    <div style="display: inline-block; background: {diff_color}15; color: {diff_color}; border: 1px solid {diff_color}40; border-radius: 9999px; padding: 0.3rem 1rem; font-size: 0.82rem; font-weight: 700;">
                        {diff}
                    </div>
                </div>
                <div style="margin-top: 0.75rem;">
                    <div style="font-size: 0.82rem; color: #9aa0ae; margin-bottom: 0.25rem;">Required Skills:</div>
                    {tags_html}
                </div>
            </div>
            """, unsafe_allow_html=True)

    else:
        st.info("Project database not found. Please ensure `database/projects.csv` exists.")


# ============================================
# PAGE: Skills Dashboard
# ============================================

elif page == "📊  Skills Dashboard":

    st.markdown("""
    <div class="hero-container fade-in" style="padding: 1rem 0;">
        <div class="hero-title" style="font-size: 2rem;">📊 Skills Dashboard</div>
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
            st.metric("📚 Total Skills", str(len(df)))
        with col2:
            st.metric("📂 Categories", str(df["category"].nunique()))
        with col3:
            easy_count = len(df[df["difficulty"] == "Easy"])
            st.metric("🟢 Beginner-Friendly", str(easy_count))

        st.markdown("<br>", unsafe_allow_html=True)

        # Skills by category
        st.markdown("### 🗂️ Skills by Category")

        categories = df["category"].unique()

        for cat in sorted(categories):
            cat_skills = df[df["category"] == cat]

            with st.expander(f"📂 {cat} ({len(cat_skills)} skills)", expanded=False):
                for _, skill in cat_skills.iterrows():
                    diff = skill.get("difficulty", "N/A")
                    diff_color = "#34d399" if diff == "Easy" else "#fbbf24" if diff == "Medium" else "#f87171"

                    st.markdown(f"""
                    <div style="display: flex; justify-content: space-between; align-items: center;
                                padding: 0.6rem 0; border-bottom: 1px solid #e0efff;">
                        <span style="font-weight: 600; color: #374151; font-family: 'Inter', sans-serif;">
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
        st.markdown("### 📊 Difficulty Distribution")

        diff_counts = df["difficulty"].value_counts()

        colors_map = {"Easy": "#34d399", "Medium": "#fbbf24", "Hard": "#f87171"}
        colors = [colors_map.get(d, "#6b7280") for d in diff_counts.index]

        fig = go.Figure(data=[go.Pie(
            labels=diff_counts.index,
            values=diff_counts.values,
            marker=dict(colors=colors, line=dict(color="white", width=3)),
            textinfo="label+percent",
            textfont=dict(family="Inter", size=14),
            hole=0.45,
        )])

        fig.update_layout(
            height=350,
            paper_bgcolor="rgba(0,0,0,0)",
            font={"family": "Inter", "color": "#374151"},
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5),
            margin=dict(l=20, r=20, t=20, b=40),
        )
        st.plotly_chart(fig, use_container_width=True)

        # Category chart
        st.markdown("### 📊 Skills per Category")

        cat_counts = df["category"].value_counts()

        fig2 = px.bar(
            x=cat_counts.index,
            y=cat_counts.values,
            labels={"x": "Category", "y": "Number of Skills"},
            color=cat_counts.values,
            color_continuous_scale=["#b8daff", "#4a94e8", "#265ea3"],
        )
        fig2.update_layout(
            height=350,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font={"family": "Inter", "color": "#374151"},
            showlegend=False,
            coloraxis_showscale=False,
            xaxis={"gridcolor": "#e0efff"},
            yaxis={"gridcolor": "#e0efff"},
            margin=dict(l=10, r=10, t=20, b=10),
        )
        st.plotly_chart(fig2, use_container_width=True)

    else:
        st.info("Skills database not found. Please ensure `database/skills.csv` exists.")
