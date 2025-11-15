# src/state.py
from typing import TypedDict, Optional, Dict, Any

class State(TypedDict):
    query: str
    search_data: Optional[Dict[str, Any]]
    answer: Optional[str]
