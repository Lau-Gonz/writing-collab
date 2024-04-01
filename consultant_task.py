import re
import requests

from crewai import Task
from bs4 import BeautifulSoup

class ConsultantTask():
  def research(self, agent):
    url = 'https://www.google.com/search?q=latest+trends+in+content+marketing'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=lambda href: href and href.startswith('/url?q=https://'))
    pages = []
    for link in links:
      match = re.search(r'(https://[^&]+)', link['href'])
      if match and 'google' not in match.group(1):
        pages.append(match.group(1))
      if len(pages)==2:
        break
    return Task(description = f"""
      Conduct an in-depth analysis on the Latest Trends In Content Marketing. Dive into recent developments, 
      focusing on innovations in digital strategies, use of technology in content creation, and standout 
      marketing campaigns from the last year. Extract key insights, statistical data, and case studies that 
      highlight the effectiveness of these trends.

      Utilize a wide range of resources such as industry-leading blogs, marketing journals, and interviews pages
      with thought leaders to ensure a well-rounded view. Your goal is to synthesize this information into 
      a comprehensive report that outlines:

      - The most impactful content marketing trends.
      - Case studies or examples of companies implementing these trends effectively.
      - Data-driven insights that demonstrate the trends’ success or areas for improvement.
      - Predictions on how these trends might evolve in the next year.
      Try to use this links:
      {pages}""",
      agent = agent,
      expected_output = """
      A detailed report on the Latest Trends In Content Marketing, including specific examples, 
      key statistics, and a forward-looking perspective. The report should be data-rich, 
      sourced from recent publications, and offer actionable insights for marketing professionals."""
    )

  def write(self, agent): 
    return Task(description = f"""
      Craft an engaging and insightful article on the Latest Trends In Content Marketing. Begin with 
      a compelling introduction that highlights the importance of staying ahead in content marketing. 
      Proceed to discuss recent trends, incorporating expert opinions, statistical evidence, and 
      real-life examples to substantiate your points.

      Your article should not only inform but also inspire marketing professionals to explore and 
      adopt these trends. Conclude with actionable advice or takeaways that readers can implement 
      in their strategies. Pay special attention to:

      - Creating a captivating title that reflects the essence of the content.
      - Ensuring the article flows smoothly from introduction to conclusion, without apparent 
      section breaks, making it a cohesive and engaging read throughout.
      - Embedding relevant keywords naturally within the text to optimize for search engines.

      Aim for concise yet comprehensive coverage, making every word count to keep the reader engaged.""",
      agent = agent,
      expected_output = """
      A compelling, well-structured article on the Latest Trends In Content Marketing that is 
      ready for publication. The article should be engaging, informative, and rich with examples 
      and data, concluding with practical advice for the audience. Ensure the content is SEO-friendly 
      and embodies a unique perspective on the topic.It should be a short article, less than 500 words, 
      do not include the word count."""
    )
