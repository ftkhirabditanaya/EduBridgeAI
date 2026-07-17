from dotenv import load_dotenv
import os

# Load .env from the project root
load_dotenv()

key = os.getenv("GOOGLE_API_KEY")

print("Key exists :", bool(key))
print("Key length :", len(key) if key else 0)
print("Key prefix :", key[:10] if key else "None")