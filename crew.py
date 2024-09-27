from crewai import Crew, Process
from agents import researcher, writer
from task import research_task, writer_task

crew = Crew(
    agents=[researcher, writer],
    tasks = [research_task, writer_task],
    process = Process.sequential,
    memory = True,
    cache = True,
    max_rpm = 100,
    share_crew = True
)
try:
    result = crew.kickoff(
        inputs={'topic':'AI VS ML VS DL vs Data Science'}
    )
    print(result)
except Exception as e:
    print(f"Error during crew kickoff")