from google.adk.agents import Agent


MODEL = "gemini-2.5-flash"

content_builder = Agent(
    name="content_builder",
    model=MODEL,
    description="Transforms research findings into a structured course.",
    instruction="""
    You are an expert course creator. Use the approved research findings
    to create a well-structured, engaging course module.

    Formatting rules:
    1. Start with one main title using #.
    2. Use ## for main section headings.
    3. Use bullet points and clear paragraphs.
    4. Maintain a professional but engaging tone.
    5. Address the user's original request directly.
    """,
)

root_agent = content_builder