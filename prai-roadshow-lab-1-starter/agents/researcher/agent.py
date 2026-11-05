from google.adk.agents import Agent
from google.adk.tools.google_search_tool import google_search


MODEL = "gemini-2.5-flash"

researcher = Agent(
    name="researcher",
    model=MODEL,
    description="Gathers information on a topic using Google Search.",
    instruction="""
    You are an expert researcher. Find comprehensive and accurate
    information on the user's topic. Summarize your findings clearly.
    If feedback says the research is insufficient, use it to refine
    your next search. Return research as text.
    """,
    tools=[google_search],
)

root_agent = researcher