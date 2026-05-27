import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def get_llm(model_name: str):
    return ChatOpenAI(
        model=model_name,
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
        temperature=0.7,
    )