# Product Research Agent

This repository is a small, practical experiment: a product research assistant built in Python. It accepts natural language product queries (for example, "best laptops under 4000"), performs web searches using a simple Tavily search tool, and calls a Groq chat model to analyze and compare results, producing a final recommendation.

The project is intentionally modular so you can swap tools (search providers, LLM providers) and extend the graph of nodes that implements the agent's workflow.

What you'll find here:
- A lightweight graph-based agent in `src/graph.py`
- LLM and tool glue in `src/agent.py`
- Small test runners (`test_graph.py`) to exercise the flow
- `vendor/` folder with minimal local stubs so the project can run even without installing all dependencies (handy for development or CI)

This README explains how to set up the project on Windows (PowerShell), how to configure API keys for Groq and Tavily, how to run and test locally, and troubleshooting tips.

## Table of contents

- Getting started
- Project structure
- Prerequisites
- Setup (PowerShell)
- Environment variables (Groq + Tavily)
- Running the app
- Running tests
- Development notes and switching providers
- Troubleshooting
- Contributing and next steps
- License

## Getting started

Follow these steps to run the project locally on Windows using PowerShell.

1. Open PowerShell and change to the project directory:

```powershell
cd "C:\Users\<you>\Desktop\New folder (4)\product-research-agent"
```

2. Create and activate a virtual environment:

```powershell
python -m venv .venv
\.\.venv\Scripts\Activate.ps1
```

3. Upgrade pip and install project dependencies (optional but recommended):

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Notes:
- If `pip install` fails with permission errors, ensure the venv is active (the prompt will show `(.venv)`), or run PowerShell with elevated privileges. Installing into the venv normally avoids system-level permission issues.
- The `vendor/` folder includes local stubs so you can run the app without installing everything; however, for real LLM and search results install the packages listed in `requirements.txt`.

## Project structure

- `main.py` — Command-line entrypoint; prompts for a query and runs the agent.
- `src/` — Primary source code
	- `agent.py` — LLM wrapper and tool functions (Groq integration point)
	- `graph.py` — Graph definition and node wiring
	- `nodes.py`, `tools.py`, `state.py` — Helper modules for nodes and tools
- `vendor/` — Local stubs (minimal `langgraph` behaviour) used for offline testing
- `requirements.txt` — Python packages required for full functionality
- `test_*.py` — Simple test runners that exercise the agent graph

## Prerequisites

- Python 3.10+ (3.11 recommended)
- Internet connection for real API calls
- Groq account and API key for LLM usage
- Tavily API key for real web search results (optional — repository provides a basic stub)

## Environment variables — Groq and Tavily

The agent uses two external services. Configure them via environment variables.

- `GROQ_API_KEY` — required for real LLM responses from Groq.
- `GROQ_MODEL` — optional, override which Groq model to use (defaults to `llama3-8b` in this repo).
- `TAVILY_API_KEY` — required for real Tavily search results.

Set them temporarily for the current PowerShell session:

```powershell
$env:GROQ_API_KEY = "gsk_...your_groq_key..."
$env:GROQ_MODEL = "llama3-8b"  # optional
$env:TAVILY_API_KEY = "tvly-...your_tavily_key..."
```

Or persist them across sessions using `setx` (you'll need to open a new PowerShell window after `setx`):

```powershell
setx GROQ_API_KEY "gsk_...your_groq_key..."
setx GROQ_MODEL "llama3-8b"
setx TAVILY_API_KEY "tvly-...your_tavily_key..."
```

Where to get your keys:
- Groq: register at https://console.groq.com and create an API key.
- Tavily: use your Tavily dashboard; this repo expects a key with a `tvly-...` prefix.

Security: Never commit API keys to source control. Use environment variables or a `.env` file that is ignored by git.

## How to run

With the venv activated and environment variables set (or not — there is a dummy fallback), run:

```powershell
python main.py
```

You will see a prompt. Example session:

```
Enter your query: find laptop under 4000
```

The agent will run the graph and print a comparison plus a final recommendation.

Behavior notes:
- If `groq` is installed and `GROQ_API_KEY` is set, the agent will call the real Groq chat model.
- If `groq` is not installed or `GROQ_API_KEY` is missing, the code returns a clear dummy response so you can continue development without an API key.

## Running tests

To run the simple graph test runner:

```powershell
python test_graph.py
```

This executes the graph with a canned query and can surface any errors in node implementations.

## Development notes and customizing providers

- Replace or extend the search tool in `src/tools.py` to integrate other providers (SerpAPI, Google, Bing).
- LLM usage is centralized in `src/agent.py`. If Groq updates their SDK, update this file accordingly.
- Graph and node wiring lives in `src/graph.py`; nodes are simple functions that accept and return a `dict`-like state.

## Troubleshooting

- `ModuleNotFoundError: No module named 'graph'` — Make sure you run `python main.py` from the project root and that the venv is activated. The `main.py` script inserts the project root and `vendor` into `sys.path` to mitigate import issues.
- Groq model decommissioned error — set `GROQ_MODEL` to a supported model (e.g. `llama3-8b`) or consult Groq's deprecation documentation.
- Permission errors during `pip install` — ensure the venv is active and you are not trying to install globally without rights.

If you hit a specific traceback, paste it here and I'll help debug it.

## Contributing

Ideas that would help the project:

- Integrate a real search provider and make the results structured (price, specs).
- Add unit tests for node functions and CI that runs tests on each PR.
- Improve error handling in graph execution and add retries for external calls.

If you'd like, I can also add:
- `.env.example` with placeholder keys
- `USAGE.md` with quick troubleshooting commands
- `requirements-dev.txt` for developer-only dependencies

## License

MIT
