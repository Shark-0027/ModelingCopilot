from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents.analysis_agent import analyze_problem
from agents.algorithm_agent import recommend_algorithm
from agents.paper_agent import generate_paper_structure


class AgentState(TypedDict):
    question: str
    analysis: str
    algorithm: str
    paper: str

def analysis_node(state: AgentState):
    result = analyze_problem(state["question"])

    return{
        "analysis": result
    }

def algorithm_node(state: AgentState):
    result = recommend_algorithm(state["analysis"])

    return{
        "algorithm": result
    }

def paper_node(state: AgentState):
    result = generate_paper_structure(state["algorithm"])

    return{
        "paper": result
    }

graph = StateGraph(AgentState)

graph.add_node("analysis", analysis_node)
graph.add_node("algorithm", algorithm_node) 
graph.add_node("paper", paper_node)

graph.set_entry_point("analysis")

graph.add_edge("analysis", "algorithm")
graph.add_edge("algorithm", "paper")
graph.add_edge("paper", END)

app = graph.compile()