import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv(dotenv_path=".env")

api_key = os.getenv("GEMINI_API_KEY")

print("API KEY FOUND:", api_key is not None)

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")