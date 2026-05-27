from backend.utils.llm import get_llm

llm = get_llm("openai/gpt-3.5-turbo")


def find_viral_angle(state):

    prompt = f"""
Topic: {state["topic"]}

Research: {state["research"]}

Analysis: {state["analysis"]}

Generate:
- 3 viral ideas
- 1 controversial angle
- 1 storytelling angle
"""

    res = llm.invoke(prompt)
    state["viral_ideas"] = res.content

    return state