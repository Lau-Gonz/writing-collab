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
        role='Principal Researcher',
        goal= 'Do amazing research and summaries based on **Latest Trends In Content Marketing**',
        backstory= "You're a Principal Researcher at a big company and you need to do research about a given topic, but focused in **Latest Trends In Content Marketing**.",
        allow_delegation=False,
        llm = Ollama(model='openhermes'))
      task = Task(
        agent=agent,
        description= f'Analyze and summarize the content below, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{text}',
        expected_output="A complete summarize."
      )
      summary = task.execute()
      return "\n\n" + summary
    return "The page you are looking for does not exist"
