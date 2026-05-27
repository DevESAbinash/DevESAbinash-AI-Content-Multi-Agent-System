from typing import TypedDict
from langgraph.graph import StateGraph, END

from backend.agents.analysis_agent import analyze_trend
from backend.agents.viral_agent import find_viral_angle
from backend.agents.script_agent import generate_script
from backend.agents.hook_agent import generate_hooks


class AgentState(TypedDict, total=False):
    topic: str
    research: list
    analysis: str
    viral_ideas: str
    script: str
    hooks: str


workflow = StateGraph(AgentState)



workflow.add_node("analysis_node", analyze_trend)
workflow.add_node("viral_node", find_viral_angle)
workflow.add_node("script_node", generate_script)
workflow.add_node("hook_node", generate_hooks)

workflow.set_entry_point("analysis_node")

workflow.add_edge("analysis_node", "viral_node")
workflow.add_edge("viral_node", "script_node")
workflow.add_edge("script_node", "hook_node")
workflow.add_edge("hook_node", END)

app = workflow.compile()
