# 🤖 AI Research Assistant Agent

An interactive CLI AI Research Agent built using Python, LangChain, Pydantic, and Web Search Tools (DuckDuckGo & Wikipedia). The agent accepts user research queries in the terminal, performs live online research, formats structured output using Pydantic, and automatically saves output to text files in `research_outputs/`.

---

## 🚀 Features

- **Interactive CLI Loop**: Enter research queries interactively directly in the terminal.
- **Web Search Integration**: Combines DuckDuckGo and Wikipedia tools.
- **Structured Data**: Enforces JSON structured responses via Pydantic (`topic`, `summary`, `sources`, `tools_used`).
- **Automatic File Export**: Saves each research output to a topic-named text file inside `research_outputs/`.

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/HasithaRathayaka/01-test-AI-Agent.git
cd 01-test-AI-Agent
```

### 2. Set up Virtual Environment
```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env` and add your GitHub Personal Access Token:
```bash
cp .env.example .env
```
In `.env`:
```env
GITHUB_TOKEN="your_github_token_here"
```

---

## 💻 Usage

Run the agent:
```bash
python main.py
```

Type any topic (e.g. `Quantum computing breakthroughs`) and press **Enter**.
To exit the interactive session, type `exit` or `quit`.
