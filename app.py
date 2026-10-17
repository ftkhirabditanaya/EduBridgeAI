"""
EduBridge AI — Application Entry Point

This module serves as the main entry point for the EduBridge AI application.
It provides both a CLI interface and launches the Streamlit web interface.

Usage:
    Run the Streamlit app:
        streamlit run streamlit_app.py

    Run via ADK:
        adk run agents

    Run via ADK Web:
        adk web
"""

import os
import sys
import subprocess


def main():
    """Launch the EduBridge AI Streamlit web interface."""

    print()
    print("=" * 50)
    print("  🎓 EduBridge AI — Starting Web Interface")
    print("=" * 50)
    print()

    streamlit_app = os.path.join(
        os.path.dirname(__file__),
        "streamlit_app.py"
    )

    if not os.path.exists(streamlit_app):
        print("Error: streamlit_app.py not found!")
        sys.exit(1)

    print("  → Launching Streamlit...")
    print("  → Open http://localhost:8501 in your browser")
    print()

    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", streamlit_app],
        cwd=os.path.dirname(__file__)
    )


if __name__ == "__main__":
    main()
