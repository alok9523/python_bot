from openai import OpenAI
from config import OPENROUTER_API_KEY

# Initialize OpenRouter Client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

def generate_ai_response(user_message: str) -> str:
    """Fetch response from OpenRouter API."""
    try:
        response = client.chat.completions.create(
            model="openai/o3-mini",
            messages=[{"role": "user", "content": user_message}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"