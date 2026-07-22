import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def parse_internship_query(user_query: str):
    """
    Uses Gemini to convert natural language
    into structured internship filters.
    """

    prompt = f"""
You are an information extraction AI.

Extract internship preferences from the user's query.

Return ONLY valid JSON.

Fields:

domain
location
branch
mode
minimum_stipend

If a field is missing, return null.

Example:

User:
I want an AI internship in Bangalore above 70000 for ECE students.

Output:

{{
"domain":"AI",
"location":"Bangalore",
"branch":"ECE",
"mode":null,
"minimum_stipend":70000
}}

Now extract from:

{user_query}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    # Remove markdown if Gemini returns ```json ... ```
    text = text.replace("```json", "")
    text = text.replace("```", "").strip()

    return json.loads(text)