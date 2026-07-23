import os
import re
from datetime import datetime
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool, Tool

# 1. DuckDuckGo Search Tool
search = DuckDuckGoSearchRun()

search_tool = Tool(
    name="search",
    func=search.run,
    description="search the web for information"
)

# 2. Wikipedia Tool
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

# Dedicated output directory for research files
OUTPUT_DIR = "research_outputs"

# 3. Custom Tool: Save to Text File inside research_outputs folder
@tool
def save_tool(data: str, file_name: str = "") -> str:
    """Saves structured research data to a text file inside the research_outputs folder."""
    try:
        # Create output directory if it doesn't exist
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if not file_name or file_name == "research_output.txt":
            clean_name = f"research_{timestamp}.txt"
        else:
            # Sanitize filename (remove illegal Windows filename characters)
            clean_name = re.sub(r'[\\/*?:"<>|]', "_", file_name)
            if not clean_name.endswith(".txt"):
                clean_name += ".txt"
            # Ensure unique filename with timestamp suffix if file already exists
            if os.path.exists(os.path.join(OUTPUT_DIR, clean_name)):
                base, ext = os.path.splitext(clean_name)
                clean_name = f"{base}_{timestamp}{ext}"

        file_path = os.path.join(OUTPUT_DIR, clean_name)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("=== Research Output ===\n")
            f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(data)
            
        return f"Successfully saved research output to {file_path}"
    except Exception as e:
        return f"Error saving to file: {e}"
