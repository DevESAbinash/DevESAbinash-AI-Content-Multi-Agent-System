from backend.utils.llm import get_llm

llm = get_llm("openai/gpt-3.5-turbo")


def generate_script(state):

    prompt = f"""
Topic: {state["topic"]}

Research: {state["research"]}

Viral Ideas: {state["viral_ideas"]}

Write:
- short video script
- hook + problem + story + CTA
"""

    res = llm.invoke(prompt)
    state["script"] = res.content

    return state