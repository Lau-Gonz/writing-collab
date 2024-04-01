from crewai import Crew, Process
from consultant_agents import ConsultantAgents
from consultant_task import ConsultantTask

if __name__ == "__main__":
  print("## Welcome to TheWritingCollab")
  print('-------------------------------')
  
  agents = ConsultantAgents()
  tasks = ConsultantTask()

  analyst_agent = agents.analyst()
  writer_agent = agents.writer()

  research_task = tasks.research(analyst_agent)
  write_task = tasks.write(writer_agent)

  crew = Crew(
    agents=[analyst_agent, writer_agent],
    tasks=[research_task, write_task],
    verbose=True,
    process=Process.sequential
  )

  result = crew.kickoff()
  print("\n\n########################")
  print("## Here is the Article")
  print("########################\n")
  print(result)