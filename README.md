#  EduBridge AI

> An AI-powered educational guidance platform built using **Google Agent Development Kit (ADK)** and **Gemini 2.5 Flash**.

EduBridge AI is a multi-agent educational assistant that helps students make informed decisions about their careers, colleges, scholarships, and study plans through intelligent AI agents.

---

#  Features

*  Career Guidance
*  College Recommendations
*  Scholarship Assistance
*  Personalized Study Planning
*  Multi-Agent Architecture using Google ADK
*  Powered by Gemini 2.5 Flash

---

#  Project Architecture

```
                    User
                      │
                      ▼
         EduBridge Coordinator Agent
                      │
      ┌───────────────┼────────────────┐
      │               │                │
      ▼               ▼                ▼
Career Agent    College Agent   Scholarship Agent
                      │
                      ▼
              Study Planner Agent
```

The coordinator agent understands the user's request and delegates it to the most suitable specialist agent.

---

#  Project Structure

```
EduBridgeAI/
│
├── edubridge/
│   ├── __init__.py
│   ├── agent.py
│   ├── career_agent.py
│   ├── college_agent.py
│   ├── scholarship_agent.py
│   └── study_planner_agent.py
│
├── app.py
├── README.md
├── .gitignore
└── .env
```

---

#  Tech Stack

| Technology       | Purpose               |
| ---------------- | --------------------- |
| Python           | Programming Language  |
| Google ADK       | Multi-Agent Framework |
| Gemini 2.5 Flash | Large Language Model  |
| Git              | Version Control       |
| GitHub           | Code Hosting          |

---

#  Installation

Clone the repository

```bash
git clone https://github.com/ftkhirabditanaya/EduBridgeAI.git
```

Move into the project

```bash
cd EduBridgeAI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GOOGLE_API_KEY=YOUR_API_KEY
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

Run the agent

```bash
adk run edubridge
```

or launch the web interface

```bash
adk web
```

---

#  Example Queries

Career Guidance

```
I am a PCB student interested in AI.
```

College Recommendation

```
Suggest Bioinformatics colleges in India.
```

Scholarships

```
Find scholarships for Biotechnology students.
```

Study Planning

```
Create a 3-month roadmap for learning Machine Learning.
```

---

#  Current Status

Current Version

*  Multi-Agent System
*  Coordinator Agent
*  Career Agent
*  College Agent
*  Scholarship Agent
*  Study Planner Agent
*  GitHub Integration

---

#  Upcoming Features

* SQLite Memory
* College Database Search
* Scholarship Database
* Tool Calling
* Streamlit Web Interface
* PDF Study Planner
* Resume Analyzer
* Career Roadmap Generator
* RAG-based Knowledge Base

---

#  Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

# License

This project is licensed under the MIT License.

---

# Author

**Khirabdi Tanaya**

Second-year Electronics and Communication Engineering student specializing in Biomedical Engineering.

Interested in Artificial Intelligence, Software Engineering, and Educational Technology.
