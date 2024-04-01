import re
import requests

from crewai import Agent, Task
from langchain_community.llms import Ollama
from langchain.tools import tool
from bs4 import BeautifulSoup

class BrowserTools():
  @tool
  def scrape_and_summarize_website(website):
    """Useful to scrape and summarize a website content"""
    response = requests.get(website)
    if response.status_code == 200:
      soup = BeautifulSoup(response.content, 'html.parser')
      text = soup.get_text()
      text = text.lower()
      text = re.sub(r'[^A-Za-z\s]+', '', text)
      text = text.replace('@', '').replace('#', '')
      agent = Agent(
        role = 'Principal Researcher',
        goal = 'To conduct insightful research and generate summaries on the Latest Trends In Content Marketing',
        backstory = """You're a Principal Researcher at a prominent company, 
        tasked with staying ahead of the Latest Trends In Content Marketing.""",
        allow_delegation=False,
        llm = Ollama(model='openhermes'))
      task = Task(
        agent = agent,
        description = f"""
        Analyze and summarize the content focusing on the most relevant Latest Trends In Content Marketing. 
        Look for insights on digital strategies, emerging technologies, and case studies of successful content marketing campaigns. 
        Structure the summary with an introduction, key findings on trends, and a conclusion highlighting the potential impact on the industry.
        CONTENT
        ----------
        {text}""",
        expected_output ="A complete summarize."
      )
      summary = task.execute()
      return "\n\n" + summary
    return "The page you are looking for does not exist."
