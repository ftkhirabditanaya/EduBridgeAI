# 🎓 EduBridge AI

> An AI-powered educational guidance platform built using **Google Agent Development Kit (ADK)** and **Gemini 2.5 Flash**.

EduBridge AI is a multi-agent educational assistant that helps students make informed decisions about their careers, colleges, scholarships, internships, and study plans through intelligent AI agents.

---

## ✨ Features

- 🧭 **Career Guidance** — AI-powered career path recommendations
- 🏫 **College Recommendations** — Find colleges with fees, rankings, and entrance exams
- 🏆 **Scholarship Assistance** — Search scholarships by eligibility
- 📚 **Personalized Study Planning** — Daily schedules and roadmaps
- 🎯 **Internship Hub** — Smart internship search with recommendation engine
- 📄 **Resume Analyzer** — ATS scoring, skill extraction, and improvement suggestions
- 📊 **ATS Scoring** — Applicant Tracking System compatibility analysis
- 🎤 **Interview Preparation** — Mock interview questions and tips
- 💡 **Project Mentor** — Portfolio project ideas for resume building
- 🧠 **Multi-Agent Architecture** — 9 specialist agents coordinated by AI

---

## 🏗️ Architecture

```
                        Student
                          │
                          ▼
            EduBridge Coordinator Agent
                          │
     ┌────────────────────┼────────────────────┐
     │        │       │       │        │        │
     ▼        ▼       ▼       ▼        ▼        ▼
  Career   College  Scholar  Study   Intern   Resume
  Agent    Agent    Agent    Planner  Agent    Agent
                                       │
                              ┌────────┼────────┐
                              ▼        ▼        ▼
                            ATS    Interview  Project
                           Agent    Agent     Mentor
```

---

## 🖥️ Tech Stack

| Technology           | Purpose                  |
| -------------------- | ------------------------ |
| Python               | Programming Language     |
| Google ADK           | Multi-Agent Framework    |
| Gemini 2.5 Flash     | Large Language Model     |
| Streamlit            | Web Interface            |
| Plotly               | Interactive Charts       |
| Pandas               | Data Processing          |
| Git/GitHub           | Version Control          |

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/ftkhirabditanaya/EduBridgeAI.git
cd EduBridgeAI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GOOGLE_API_KEY=YOUR_API_KEY
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

---

## ▶️ Running

### Streamlit Web Interface

```bash
streamlit run streamlit_app.py
```

### Via ADK

```bash
adk run agents
```

### Via ADK Web

```bash
adk web
```

---

## 📸 Screenshots

The web interface features a **light blue pastel & cream** theme with:

- Glassmorphism panels and gradient headers
- Interactive Plotly charts for salary, fees, and stipend comparisons
- Card-based layouts with hover animations
- AI-powered chat with the EduBridge coordinator
- Resume upload with ATS scoring gauges

---

## 📂 Project Structure

```
EduBridgeAI/
├── agents/
│   ├── __init__.py
│   ├── agent.py                  # Coordinator (root agent)
│   ├── career_agent.py           # Career guidance specialist
│   ├── college_agent.py          # College recommendations
│   ├── scholarship_agent.py      # Scholarship search
│   ├── study_planner_agent.py    # Study planning
│   ├── internship_agent.py       # Internship recommendations
│   ├── resume_agent.py           # Resume analysis
│   ├── ats_agent.py              # ATS scoring
│   ├── interview_agent.py        # Interview preparation
│   └── project_mentor_agent.py   # Project mentorship
│
├── tools/
│   ├── __init__.py
│   ├── career_tool.py            # Career database search
│   ├── college_tool.py           # College database search
│   ├── scholarship_tool.py       # Scholarship database search
│   ├── internship_tool.py        # Internship search engine
│   ├── resume_parser.py          # PDF/DOCX/TXT extraction
│   ├── resume_analyzer.py        # Skill & experience extraction
│   ├── ats_scorer.py             # ATS compatibility scoring
│   ├── query_parser.py           # NL query to structured filters
│   ├── normalizer.py             # Filter value normalization
│   ├── recommendation_engine.py  # Match score calculation
│   └── recommendation_resume.py  # Resume-based recommendations
│
├── database/
│   ├── careers.csv
│   ├── colleges.csv
│   ├── internships.csv
│   ├── scholarships.csv
│   ├── projects.csv
│   └── skills.csv
│
├── assets/
│   ├── styles.css                # Custom CSS theme
│   └── logo.png
│
├── .streamlit/
│   └── config.toml               # Streamlit theme configuration
│
├── streamlit_app.py              # Main Streamlit frontend
├── app.py                        # Application entry point
├── requirements.txt              # Python dependencies
├── .env                          # API keys (not tracked)
├── .gitignore
└── README.md
```

---

## 💬 Example Queries

**Career Guidance:**
```
I am a PCB student interested in AI. What careers can I pursue?
```

**College Recommendation:**
```
Suggest Bioinformatics colleges in India.
```

**Scholarships:**
```
Find scholarships for Engineering students.
```

**Study Planning:**
```
Create a 3-month roadmap for learning Machine Learning.
```

**Interview Prep:**
```
How do I prepare for a Google software engineering interview?
```

---

## 👩‍💻 Author

**Khirabdi Tanaya**

Second-year Electronics and Communication Engineering student specializing in Biomedical Engineering.

Interested in Artificial Intelligence, Software Engineering, and Educational Technology.

---

## 📝 License

This project is licensed under the MIT License.
