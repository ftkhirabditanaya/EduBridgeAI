from google import genai
import os
from dotenv import load_dotenv

load_dotenv("edubridge/.env")

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello in one sentence."
)

print(response.text)