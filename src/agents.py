from crewai import Agent
from tools import medical_search

MODEL_NAME = "groq/llama-3.3-70b-versatile"

researcher = Agent(
    role="Senior Medical Researcher",
    goal="Find recent (2024–2026) ischemic stroke clinical trials",
    backstory="Expert in medical literature and clinical research",
    tools=[medical_search],
    verbose=True,
    llm=MODEL_NAME
)

analyst = Agent(
    role="Clinical Analyst",
    goal="Evaluate efficacy and safety of treatments",
    backstory="Specialist in clinical data interpretation",
    verbose=True,
    llm=MODEL_NAME
)

writer = Agent(
    role="Medical Communicator",
    goal="Write a professional medical report in Markdown",
    backstory="Experienced medical writer",
    verbose=True,
    llm=MODEL_NAME
)
