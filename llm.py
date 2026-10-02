from groq import Groq
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Get Groq API key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)


def analyze_news(headlines):
    context = "\n".join(headlines)

    prompt = f"""
You are a financial news sentiment analyzer.

Analyze the following news headlines about a stock:

{context}

Based only on these headlines:

1. Determine the overall sentiment: Positive, Negative, or Neutral.
2. Determine the stock signal: Bullish, Bearish, or Neutral.
3. Give a short reason for your decision.

Return the answer in this format:

Sentiment: <Positive/Negative/Neutral>
Signal: <Bullish/Bearish/Neutral>
Reason: <short explanation>
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content