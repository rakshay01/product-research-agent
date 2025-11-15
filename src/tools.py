import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

from tavily import TavilyClient

api_key = os.getenv("TAVILY_API_KEY")
print("Loaded API KEY:", api_key)   # TEMPORARY DEBUG

tavily_client = TavilyClient(api_key=api_key)

def search_tool(query: str):
    print("🔍 Running Tavily search...")
    return tavily_client.search(query=query)
