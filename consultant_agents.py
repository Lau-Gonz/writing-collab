from crewai import Agent
from tools.browser_tools import BrowserTools
from langchain_community.llms import Ollama

class ConsultantAgents():
  def analyst(self):
    return Agent(
      role='The Best Research Analyst',
      goal="""To conduct in-depth analysis and provide valuable insights""",
      backstory="""As a seasoned research analyst, your expertise lies in conducting 
      comprehensive investigations and analyzing data from various sources. 
      You're adept at extracting key insights and presenting them in a clear and concise 
      manner.""",
      verbose=True,
      allow_delegation = False,
      llm = Ollama(model='openhermes'),
      tools=[
        BrowserTools.scrape_and_summarize_website,
      ]
    )

  def writer(self):
    return Agent(
      role='The Best Content Writer',
      goal="""To create captivating content that informs and engages readers""",
      backstory="""As a skilled content writer, you excel at crafting compelling 
      narratives that captivate audiences. Your expertise lies in research, 
      interpretation of data, and delivering information in an intriguing manner. 
      Currently, you've been assigned an important project with a high-profile client""",
      verbose=True,
      allow_delegation = False,
      llm = Ollama(model='openhermes'),
  )
