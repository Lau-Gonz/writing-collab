from crewai import Task

class ConsultantTask():
  def research(self, agent):
    return Task(description="""
        Conduct a thorough investigation centered around the chosen topic: **Latest Trends
        In Content Marketing**. Utilize various resources including web pages, news 
        articles, and other relevant sources to collect pertinent information.
        
        Pay close attention to identifying and analyzing keywords within the gathered 
        data to ensure a comprehensive understanding.
        
        The ultimate objective is to provide a succinct overview of the topic: **Latest Trends
        In Content Marketing** along with the key insights and findings derived from the research.
        
        Please ensure that the information gathered is based on the most recent and 
        up-to-date data available.
      """,
      agent=agent,
      expected_output="""
        A document summarizing the findings of the research in **Latest Trends
        In Content Marketing**. The document should relevant data points and a concise overview 
        of the topic. The information must be current and accurately reflect the latest 
        trends related to the topic.
      """
    )

  def write(self, agent): 
    return Task(description=f"""
        Create an engaging article focusing on the chosen topic: **Latest Trends
        In Content Marketing**. This includes crafting a captivating title, identifying
        relevant keywords, and structuring the article with a clear introduction, development 
        and conclusion. The article should be concise yet informative, designed to capture 
        and maintain the interest of the readers. Ensure that it provides a unique 
        perspective on the topic.
        
        The final deliverable should be a well-structured article, presented as a 
        cohesive piece of text without separations for each section.The text presented must be short, 
        clear and concise. It seeks to attract and conquer the reader, it cannot be extended in text.
      """,
      agent=agent,
      expected_output="""
        A complete article that adheres to the instructions provided. The article 
        should have a compelling title, include identified keywords, and be structured 
        with an introduction, body, and conclusion. It should offer a unique perspective 
        on the topic **Latest Trends In Content Marketing** and engage readers from start
        to finish. The article must be presented as a single, cohesive text suitable for publication,
        presented as a cohesive piece of text without separations for each section.
      """
    )
