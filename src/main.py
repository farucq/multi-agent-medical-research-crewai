from crewai import Crew, Process
from tasks import research_task, analysis_task, writing_task

crew = Crew(
    agents=[
        research_task.agent,
        analysis_task.agent,
        writing_task.agent
    ],
    tasks=[
        research_task,
        analysis_task,
        writing_task
    ],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

with open("report.md", "w") as f:
    f.write(str(result))

print(" report.md generated successfully")
