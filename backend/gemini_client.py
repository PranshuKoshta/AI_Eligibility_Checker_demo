from google import genai
from google.genai import types

from config import GEMINI_API_KEY

DEFAULT_GEMINI_MODEL_1 = "gemini-3.1-flash-lite-preview"
DEFAULT_GEMINI_MODEL_2 = "gemma-4-31b-it"


client = genai.Client(api_key=GEMINI_API_KEY)


def generate_ai_summary(prompt: str, model: str = DEFAULT_GEMINI_MODEL_1) -> str:
    response = client.models.generate_content(
        model=model,
        contents=prompt,
         config=types.GenerateContentConfig(
        temperature=0.5, 
        max_output_tokens=512
    )
    )
    return response.text or ""