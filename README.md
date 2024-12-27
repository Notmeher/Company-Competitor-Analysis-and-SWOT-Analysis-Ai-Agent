# Company Competitor Service Analysis and SWOT AI Agent

## Overview
This project is a multi-agent system designed to automate company research, competitor analysis, and SWOT analysis. It uses OpenAI's GPT-4 and a set of interconnected agents to extract, analyze, and present actionable insights from a company’s online presence. The application is built using Python, Streamlit, and CrewAI.
![app-12-26-2024_04_24_PM](https://github.com/user-attachments/assets/e23232ca-c2e1-48fe-a0b4-defe026f1140)
## Features
1. **Company Details Extraction**: Scrapes the company name and text content from a given URL.
2. **Service Analysis**: Extracts key services, products, or technologies from the company's description.
3. **Competitor Analysis**: Identifies competitors based on the company's services and provides their website links.
4. **SWOT Analysis**:
   - Performs a SWOT analysis (Strengths, Weaknesses, Opportunities, Threats) for the company.
   - Optionally conducts a SWOT analysis for the first identified competitor.
5. **Interactive Streamlit Interface**: Provides a user-friendly interface for URL input and results visualization.

## Tech Stack
- **Python**
- **Streamlit**
- **OpenAI GPT-4 API**
- **BeautifulSoup** (for web scraping)
- **Pandas** (for data processing)
- **CrewAI** (for multi-agent coordination)

## Installation
### Prerequisites
1. Python 3.8+
2. OpenAI API Key
3. Internet connection

### Steps
1. Clone the repository:
   ```bash
   gh repo clone 
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## How to Use
1. Launch the Streamlit application.
2. Enter the URL of the company website you want to analyze.
3. Click the "Analyze Competitors, Services, and SWOT" button.
4. View the results, including:
   - Company name
   - Extracted services
   - Competitors with links
   - SWOT analysis for the company
   - SWOT analysis for the first identified competitor (if applicable).

## Project Structure
```
competitor-analysis-agent/
│
├── app.py                # Streamlit application
├── tasks.py              # Task definitions for scraping, analysis, and SWOT
├── tools.py              # Utility functions for web scraping
├── requirements.txt      # Python dependencies
├── .env.example          # Example environment file
└── README.md             # Project documentation
```

## Agents
### 1. **Company Researcher**
   - Role: Extracts company details (name and body text) from the given URL.
   - Memory: Enabled
   - Delegation: Disabled

### 2. **Market Analyst**
   - Role: Analyzes services and identifies competitors.
   - Memory: Enabled
   - Delegation: Disabled

### 3. **Business Analyst**
   - Role: Performs a SWOT analysis for the company.
   - Memory: Enabled
   - Delegation: Disabled

## Key Functions
### 1. `crew_workflow(url)`
- Orchestrates the scraping, analysis, and SWOT tasks.
- Returns results for Streamlit display.

### 2. `scraping_task(inputs)`
- Extracts company name and description from the provided URL.

### 3. `analysis_task(inputs)`
- Extracts services and identifies competitors based on the company's description.

### 4. `swot_task(inputs)`
- Performs a SWOT analysis for the company using extracted data.

## Example Input And Outputs
![app-12-26-2024_04_23_PM](https://github.com/user-attachments/assets/8bfe1542-aa89-4a88-871e-e2d118bacbb8)
## License
This project is licensed under the MIT License.

## Acknowledgments
- OpenAI for the GPT-4 API
- Streamlit for the interactive framework
- BeautifulSoup for web scraping utilities

---
For any issues or feature requests, feel free to open an issue or contribute to the repository!
