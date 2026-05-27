from backend.utils.llm import get_llm

llm = get_llm("openai/gpt-3.5-turbo")


def generate_hooks(state):

    prompt = f"""
Topic: {state["topic"]}

Script: {state["script"]}

Generate 10 viral hooks:
- curiosity
- emotional
- high CTR
"""

    res = llm.invoke(prompt)
    state["hooks"] = res.content

    return state