from crewai import Agent

# Agent for fetching company details
company_researcher = Agent(
    role='Company Researcher',
    goal='Extract company details from the given URL.',
    verbose=True,
    memory=True,
    tools=[],  # No tools required for scraping in this agent
    allow_delegation=False
)

# Agent for competitor analysis
market_analyst = Agent(
    role='Market Analyst',
    goal='Analyze services and identify competitors from extracted data.',
    verbose=True,
    memory=True,
    tools=[],  # OpenAI API logic will be in the task
    allow_delegation=False
)

# Agent for SWOT analysis
business_analyst = Agent(
    role='Business Analyst',
    goal='Perform a SWOT analysis for the company based on extracted data.',
    verbose=True,
    memory=True,
    tools=[],  # OpenAI API logic will be in the task
    allow_delegation=False
)
