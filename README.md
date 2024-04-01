# TheWritingCollab

Welcome to TheWritingCollab! This GitHub repository is dedicated to assisting in the creation of compelling articles through the automated collection and analysis of online data. By utilizing CrewAI and Ollama, our project streamlines the process of generating insightful content for developers, researchers, and professionals who require efficient web scraping and text generation capabilities.

## Project Description

TheWritingCollab leverages CrewAI to automate tasks and agents, integrating advanced web analysis with BeautifulSoup for HTML parsing and `requests` for web queries. This structure is designed to support specific consulting tasks, utilizing web scraping and content analysis to derive meaningful insights. It's an ideal tool for those looking to automate data collection, content analysis, and text generation processes.

## Project Structure

- **main.py**: Serves as the entry point of the project. It initiates the execution by coordinating consulting agents with their respective tasks.
- **browser_tools.py**: Offers a comprehensive interface for conducting complex web scraping and analysis operations, employing BeautifulSoup for HTML parsing.
- **consultant_agents.py**: Defines `ConsultantAgents` as automated agents designed to execute specific tasks using `BrowserTools`.
- **consultant_task.py**: Establishes `ConsultantTask`, outlining the tasks these agents perform, including specific scraping and analysis logic.

## Running the Project

For local execution, the project employs Openhermes[^1], an open-source LLM, and relies on `ollama`[^2] for installation. To download Openhermes using `ollama`, input the following command:

```bash
ollama pull openhermes
```

Setting up the execution environment requires Python 3.11[^4] or higher and `poetry`[^3] for dependency management. Once these prerequisites are installed, execute these commands in your terminal:

```bash
poetry env use python3.11
poetry install
poetry shell
```

### Main Dependencies

- **crewai**: For automating the creation and management of agents and tasks.
- **BeautifulSoup**: For parsing and analyzing HTML documents.
- **requests**: For making HTTP requests.

## Usage

To generate an article, simply run the main file after setting up the environment:

```bash
python main.py
```

## References

- [^1]: [Openhermes on Huggingface](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B)
- [^2]: [Ollama GitHub Repository](https://github.com/ollama/ollama)
- [^4]: [Poetry Installation Guide](https://python-poetry.org/docs/)
- [^3]: [Python Official Versions](https://www.python.org/doc/versions/)
