# src/nodes.py

from typing import Dict, Any
from .tools import search_tool

def search_node(state: Dict[str, Any]) -> Dict[str, Any]:
    query = state["query"]
    print("🔍 Running Tavily search...")

    result = search_tool(query)

    return {
        "search_data": result
    }


from .agent import run_llm

def llm_node(state: Dict[str, Any]) -> Dict[str, Any]:
    print("🤖 Generating final recommendation...")

    query = state["query"]
    search_data = state["search_data"]

    llm_input = f"""
    You are a product research expert.

    User Query: {query}

    Search Data:
    {search_data}

    Task:
    - Compare products
    - Make a clean table
    - Give final recommendation
    """

    response = run_llm(llm_input)

    return {
        "answer": response
    }
