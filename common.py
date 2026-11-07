"""Shared Gemini connection. Used by both weekly apps."""
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def get_client():
    key = os.getenv("GEMINI_API_KEY", "").strip()
    if not key or key == "replace_with_your_own_key":
        raise ValueError("Add your Gemini API key to the .env file first.")
    return genai.Client(api_key=key)

def get_model():
    return os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")
