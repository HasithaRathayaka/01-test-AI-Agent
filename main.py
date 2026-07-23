import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

try:
    from langchain.agents import create_tool_calling_agent, AgentExecutor
except ImportError:
    from langchain_classic.agents import create_tool_calling_agent, AgentExecutor

from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    openai_api_key=os.getenv("GITHUB_TOKEN"),
    openai_api_base="https://models.inference.ai.azure.com"
)

tools = [search_tool, wiki_tool, save_tool]
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a research assistant that will help generate a research paper. Answer the user query and use the necessary tools. Save your final research output to a text file using save_tool (pass a short descriptive file_name based on the topic, e.g., 'ai_breakthroughs.txt'). Wrap the final response in this format and provide no other text:\n{format_instructions}"),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}"),
]).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

if __name__ == "__main__":
    print("=" * 60)
    print("Welcome to the AI Research Assistant Agent!")
    print("All research outputs will be saved in the 'research_outputs' folder.")
    print("Enter a topic/question to research, or type 'exit' to quit.")
    print("=" * 60)

    while True:
        try:
            user_query = input("\nEnter your research query: ").strip()
            if not user_query:
                continue
            if user_query.lower() in ["exit", "quit", "q"]:
                print("Goodbye!")
                break

            print(f"\nProcessing research for: '{user_query}'...\n")
            raw_response = agent_executor.invoke({"query": user_query})
            
            output_str = raw_response.get("output", "")
            
            try:
                structured_response = parser.parse(output_str)
                print("\n--- STRUCTURED RESEARCH RESULT ---")
                print(f"Topic:      {structured_response.topic}")
                print(f"Summary:    {structured_response.summary}")
                print(f"Sources:    {', '.join(structured_response.sources)}")
                print(f"Tools Used: {', '.join(structured_response.tools_used)}")
            except Exception as parse_err:
                print("\n--- RAW AGENT RESPONSE ---")
                print(output_str)

        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break
