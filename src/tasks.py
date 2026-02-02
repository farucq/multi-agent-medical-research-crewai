from crewai import Task
from agents import researcher, analyst, writer

research_task = Task(
    description="Research latest ischemic stroke treatments and clinical trials (2024–2026)",
    expected_output="Bullet-point research findings",
    agent=researcher
)

analysis_task = Task(
    description="Analyze efficacy, safety, and clinical relevance",
    expected_output="Clinical analysis summary",
    agent=analyst
)

writing_task = Task(
    description="Generate a structured Markdown medical report",
    expected_output="Markdown report",
    agent=writer
)
