from google import genai
from dotenv import load_dotenv
import os

# Load .env from project root
load_dotenv()

key = os.getenv("GOOGLE_API_KEY")

print("Key exists:", bool(key))
print("Key length:", len(key) if key else 0)

client = genai.Client(api_key=key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello in one sentence."
)

print(response.text)