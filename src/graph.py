
from langgraph.graph import StateGraph, END
from .state import State
from .nodes import search_node, llm_node

# Build the graph
graph = StateGraph(State)

# Add nodes
graph.add_node("search", search_node)
graph.add_node("llm", llm_node)

# Add flow
graph.set_entry_point("search")
graph.add_edge("search", "llm")
graph.add_edge("llm", END)

# Compile the graph
app = graph.compile()
