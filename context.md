# Project Blueprint: AI Research Agent

## Overview
An interactive CLI AI Research Agent built using Python, LangChain, Pydantic, and Web Search Tools. The agent accepts user input interactively in the terminal, conducts online research via tools, returns structured data, and automatically saves every search result into a dedicated `research_outputs/` directory with topic-specific filenames.

---

## Completed Features & Architecture

1. **Environment Setup**
   - Active virtual environment (`venv`).
   - Dependencies: `python-dotenv`, `langchain-openai`, `langchain`, `langchain-community`, `pydantic`, `wikipedia`, `duckduckgo-search`, `ddgs`.

2. **LLM Connection**
   - Loads `GITHUB_TOKEN` from `.env`.
   - Connected to `gpt-4o-mini` via `https://models.inference.ai.azure.com`.

3. **Structured Output Definition**
   - Pydantic model (`ResearchResponse`):
     - `topic`: `str`
     - `summary`: `str`
     - `sources`: `list[str]`
     - `tools_used`: `list[str]`

4. **Prompt Engineering**
   - `ChatPromptTemplate` with system prompt framing AI as a research assistant.
   - Formatted using `PydanticOutputParser.get_format_instructions()`.

5. **Built-in Tools (`tools.py`)**
   - `search_tool`: DuckDuckGo web search wrapper.
   - `wiki_tool`: Wikipedia API wrapper.

6. **Custom Tool (`tools.py`)**
   - `@tool save_tool`: Creates `research_outputs/` directory and saves every search to a topic-named `.txt` file (with timestamp fallbacks).

7. **Interactive Agent Execution Loop (`main.py`)**
   - `create_tool_calling_agent` + `AgentExecutor`.
   - `while True:` loop reading user queries via `input("\nEnter your research query: ")`.
