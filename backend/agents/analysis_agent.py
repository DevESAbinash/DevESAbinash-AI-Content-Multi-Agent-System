from backend.utils.llm import get_llm
from backend.utils.research import search_topic
#i am using openai/gpt-3.5-turbo but you can use other models for more better result
llm = get_llm("openai/gpt-3.5-turbo")


def analyze_trend(state):

    topic = state["topic"]
    research = search_topic(topic)

    state["research"] = research

    prompt = f"""
Topic: {topic}

Research:
{research}

Task:
- audience psychology
- viral opportunities
- creator angles
- best platform strategy
"""

    res = llm.invoke(prompt)
    state["analysis"] = res.content

    return state