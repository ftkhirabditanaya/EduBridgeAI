# EduBridge AI

An enterprise-grade, multi-agent educational counseling and career guidance platform built using the Google Agent Development Kit (ADK) and Gemini 2.5 Flash.

EduBridge AI orchestrates a network of specialized autonomous agents to deliver data-driven guidance on career pathways, higher education admissions, financial aid, internship acquisition, ATS resume optimization, and technical interview readiness.

---

## Overview

EduBridge AI solves the problem of fragmented educational counseling by bringing together nine specialized agents under a centralized coordinator. The system ingests structured academic datasets, performs natural language query parsing, analyzes unstructured resume documents, and calculates multi-criteria recommendation scores to provide actionable roadmaps for students and early-career professionals.

---

## Core Capabilities

- **Career Exploration Engine**: Contextual recommendations mapping educational backgrounds (e.g., STEM, PCB, Commerce) to emerging industry specializations with salary benchmarks and growth trends.
- **Academic Institution Discovery**: Multi-parameter search across accredited universities, covering admission requirements, fee structures, national rankings, and entrance examinations.
- **Financial Aid & Scholarship Search**: Automated matching of candidates against eligibility criteria for institutional, governmental, and private scholarships.
- **Personalized Academic Roadmaps**: Structured milestone generation providing daily study schedules, curriculum pacing, and skill progression tracking.
- **Internship Matching System**: Weighted multi-factor recommendation engine scoring opportunities against user competencies, academic disciplines, and location preferences.
- **ATS Resume Parser & Diagnostics**: Ingestion of PDF, DOCX, and text resumes with structural parsing, keyword density evaluation, format compliance checking, and quantifiable scoring.
- **Technical Interview Simulation**: Dynamic generation of role-specific technical and behavioral questions accompanied by evaluation criteria and model answers.
- **Project Mentorship & Portfolio Advisory**: Curated capstone and technical project recommendations designed to address resume skill gaps.

---

## System Architecture

EduBridge AI implements a hierarchical multi-agent pattern orchestrated through the Google Agent Development Kit.

```
                                  Student / User
                                        │
                                        ▼
                         EduBridge Coordinator Agent
                          (Root Orchestrator / LLM)
                                        │
        ┌──────────────┬────────────────┼──────────────┬──────────────┐
        │              │                │              │              │
        ▼              ▼                ▼              ▼              ▼
  Career Agent   College Agent  Scholarship Agent Study Planner  Internship Agent
  (Guidance)     (Admissions)     (Financial)       (Roadmaps)     (Opportunities)
                                                                      │
                                                ┌─────────────────────┼─────────────────────┐
                                                │                     │                     │
                                                ▼                     ▼                     ▼
                                           Resume Agent           ATS Agent          Interview Agent
                                           (Extraction)         (Scoring Engine)     (Mock Evaluation)
                                                │
                                                ▼
                                       Project Mentor Agent
                                       (Portfolio Advisory)
```

### Agent Responsibilities

| Agent | Responsibility | Primary Tooling |
| :--- | :--- | :--- |
| **Coordinator Agent** | Request triage, intent classification, multi-agent dispatch | Google ADK Router |
| **Career Agent** | Career trajectory and specialization analysis | `career_tool.py`, Database Registry |
| **College Agent** | University comparisons, entrance cutoffs, and fees | `college_tool.py` |
| **Scholarship Agent** | Financial aid eligibility verification | `scholarship_tool.py` |
| **Study Planner Agent** | Time-bound study roadmap synthesis | Dynamic Curriculum Generator |
| **Internship Agent** | Opportunity ranking and match scoring | `internship_tool.py`, `recommendation_engine.py` |
| **Resume Agent** | Text extraction, entity recognition, and section parsing | `resume_parser.py`, `resume_analyzer.py` |
| **ATS Agent** | Algorithmic Applicant Tracking System scoring | `ats_scorer.py` |
| **Interview Agent** | Technical and behavioral question generation | Gemini Evaluator |
| **Project Mentor Agent** | Portfolio project suggestions based on skill deficits | Project Knowledge Base |

---

## Technology Stack

| Layer | Component | Description |
| :--- | :--- | :--- |
| **Core Runtime** | Python 3.10+ | Primary language environment |
| **Agent Framework** | Google Agent Development Kit (ADK) | Multi-agent coordination and lifecycle management |
| **Language Model** | Gemini 2.5 Flash | High-throughput, low-latency reasoning and evaluation |
| **Web Presentation** | Streamlit | Responsive dashboard with light pastel theme |
| **Data Visualization** | Plotly | Interactive financial, salary, and score distribution charts |
| **Document Processing**| pdfplumber, python-docx | Extraction of unstructured resume files |
| **Data Engine** | Pandas, NumPy | Structured tabular queries and weighted match matrices |

---

## Directory Structure

```
EduBridgeAI/
├── agents/
│   ├── __init__.py
│   ├── agent.py                  # Root Coordinator Agent
│   ├── career_agent.py           # Career Guidance Agent
│   ├── college_agent.py          # College Admissions Agent
│   ├── scholarship_agent.py      # Scholarship & Aid Agent
│   ├── study_planner_agent.py    # Academic Planning Agent
│   ├── internship_agent.py       # Internship Matching Agent
│   ├── resume_agent.py           # Document Extraction Agent
│   ├── ats_agent.py              # ATS Scoring Agent
│   ├── interview_agent.py        # Mock Interview Agent
│   └── project_mentor_agent.py   # Project Mentorship Agent
│
├── tools/
│   ├── __init__.py
│   ├── career_tool.py            # Career database queries
│   ├── college_tool.py           # College database queries
│   ├── scholarship_tool.py       # Scholarship criteria matcher
│   ├── internship_tool.py        # Internship dataset search engine
│   ├── resume_parser.py          # PDF / DOCX / TXT text extraction
│   ├── resume_analyzer.py        # Skill extraction and gap analysis
│   ├── ats_scorer.py             # Rule-based and semantic ATS scoring
│   ├── query_parser.py           # Natural language to structured query filter
│   ├── normalizer.py             # Entity and filter normalization
│   ├── recommendation_engine.py  # Multi-factor similarity scoring
│   └── recommendation_resume.py  # Profile-to-internship matching
│
├── database/
│   ├── careers.csv               # Curated career tracks and compensation data
│   ├── colleges.csv              # Accredited institutions, programs, and fees
│   ├── internships.csv           # Opportunities, requirements, and stipends
│   ├── scholarships.csv          # Aid programs, deadlines, and eligibility
│   ├── projects.csv              # Portfolio project specifications
│   └── skills.csv                # Skill taxonomy and aliases
│
├── assets/
│   ├── styles.css                # Custom application stylesheet
│   └── logo.png                  # Platform branding assets
│
├── .streamlit/
│   └── config.toml               # Streamlit server and theme configuration
│
├── uploads/                      # Temporary storage for resume parsing
├── app.py                        # Unified application launcher
├── streamlit_app.py              # Full-featured Streamlit web application
├── requirements.txt              # Production dependency specifications
├── .env.example                  # Environment configuration template
├── .gitignore                    # Git tracking rules
└── README.md                     # Technical documentation
```

---

## Installation and Setup

### Prerequisites

- Python 3.10 or higher
- Google Cloud / Gemini API key
- Git

### 1. Repository Setup

Clone the repository to your local environment:

```bash
git clone https://github.com/ftkhirabditanaya/EduBridgeAI.git
cd EduBridgeAI
```

### 2. Virtual Environment Configuration

Create and activate an isolated virtual environment:

```bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Dependency Installation

Install all required packages:

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the project root directory with your credentials:

```ini
GOOGLE_API_KEY=your_gemini_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

---

## Running the Application

### Option A: Streamlit Web Dashboard (Recommended)

To run the interactive web application:

```bash
streamlit run streamlit_app.py
```

The application will be accessible at `http://localhost:8501`.

### Option B: Unified Application Entry Point

To start via the standard project launcher:

```bash
python app.py
```

### Option C: Google ADK CLI Execution

To run the multi-agent coordinator directly through the Google Agent Development Kit:

```bash
adk run agents
```

To launch the ADK built-in web viewer:

```bash
adk web
```

---

## Example Usage

### Career Guidance Inquiries
```text
"I have completed my secondary education with Physics, Chemistry, and Biology. What interdisciplinary career tracks exist in Computational Biology and Bioinformatics?"
```

### College Admissions Inquiries
```text
"List top-ranked institutions in India offering Master's degrees in Data Science with annual tuition under 3 Lakh INR."
```

### Scholarship Search Inquiries
```text
"What merit-based scholarships are available for female undergraduate students pursuing Computer Science?"
```

### Study Roadmap Inquiries
```text
"Construct a comprehensive 12-week study schedule for transitioning from Python fundamentals to Deep Learning."
```

### Interview Preparation Inquiries
```text
"Generate five technical interview questions focused on distributed systems and system design for a Mid-Level Software Engineer role."
```

---

## Testing

Execute the test suite to validate tool integrity and scoring algorithms:

```bash
# Verify internship recommendation matching logic
python test_internship_tool.py

# Verify resume parsing and recommendation engine
python test_resume_recommendation.py

# Verify similarity scoring calculations
python test_recommendation_engine.py
```

---

## Author

**Khirabdi Tanaya**  
Undergraduate Student in Electronics and Communication Engineering (Specialization in Biomedical Engineering)  
Research Interests: Artificial Intelligence, Autonomous Multi-Agent Systems, Educational Technology.

---

## License

This project is distributed under the terms of the MIT License. See `LICENSE` for details.
