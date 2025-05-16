import os
from crewai import Agent
from tools import tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# call gemini model
llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash-preview-04-17',
                            verbose=True,
                            temperature=0.5,
                            goggle_api_key=os.getenv('GOOGLE_API_KEY'))               

# create a senior researcher agent with memory and verbose mode

news_researcher = Agent(
        role="Senior Researcher",
        goal="Uncover ground breaking technologies in {topic}",
        verbose=True,
        memory=True,
        backstory=( "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
        ),
        tools=[tool],
        llm=llm,
        allow_delegation=True
)

# creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
         "With a flair for simplifying complex topics, you craft"
         "engaging narratives that captivate and educate, bringing new"
         "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)


market_analyst = Agent(
        role="Market Analyst",
        goal=(
            "Analyze the market size, existing solutions, and solution categories for '{topic}'. "
            "Use search tools to gather current and reliable data."
        ),
        backstory=(
            "You are an expert in market research with a knack for identifying market trends, "
            "estimating market sizes, and categorizing solutions. You rely on search tools to "
            "ground your findings in credible sources like market reports and industry articles."
        ),
        verbose=True,
        memory=True,
        llm=llm,
        tools=[tool],
        allow_delegation=False
    )

company_analyst = Agent(
        role="Company Analyst",
        goal=(
            "Analyze the competitive landscape for '{topic}' by identifying key companies, "
            "their solutions, and market shares. Ground all findings in search data."
        ),
        backstory=(
            "You specialize in competitive intelligence, with expertise in dissecting company "
            "portfolios, estimating market shares, and analyzing financial performance using "
            "search tools to find reports, briefings, and news."
        ),
        verbose=True,
        memory=True,
        llm=llm,
        tools=[tool],
        allow_delegation=False
    )

regional_analyst = Agent(
        role="Regional Analyst",
        goal=(
            "Analyze solution preferences and revenue distribution for '{topic}' across continents. "
            "Use search tools to identify regional trends and financial estimates."
        ),
        backstory=(
            "You are a regional market expert skilled at identifying geographical trends, "
            "solution preferences, and revenue distributions. You use search tools to find "
            "regional reports and market analyses."
        ),
        verbose=True,
        memory=True,
        llm=llm,
        tools=[tool],
        allow_delegation=False
    )

country_analyst = Agent(
        role="Country Analyst",
        goal=(
            "Analyze solution preferences and revenue for '{topic}' in the top 20 countries. "
            "Use search tools to gather country-specific data."
        ),
        backstory=(
            "You excel at country-level market analysis, pinpointing solution preferences, "
            "revenue estimates, and key players. You rely on search tools for country-specific "
            "reports and news."
        ),
        verbose=True,
        memory=True,
        llm=llm,
        tools=[tool],
        allow_delegation=False
    )

strategy_consultant = Agent(
        role="Strategy Consultant",
        goal=(
            "Synthesize findings for '{topic}' and propose a strategic solution or market entry approach. "
            "Base recommendations on comprehensive data analysis."
        ),
        backstory=(
            "You are a seasoned strategy consultant with a talent for synthesizing complex data "
            "into actionable insights. You identify market gaps and craft strategic recommendations "
            "grounded in thorough analysis."
        ),
        verbose=True,
        memory=True,
        llm=llm,
        tools=[tool],
        allow_delegation=False
    )



# Single comprehensive analyst agent
comprehensive_analyst = Agent(
    role="Comprehensive Market and Strategy Analyst",
    goal=(
        "Conduct an in-depth analysis of '{topic}', covering groundbreaking technologies, market size, competitive landscape, "
        "regional and country-specific preferences, and strategic recommendations. Produce compelling narratives and actionable insights."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a versatile expert combining skills in research, writing, market analysis, competitive intelligence, and strategic consulting. "
        "Driven by curiosity, you uncover innovative technologies, analyze market trends, and craft engaging stories. "
        "With a knack for synthesizing complex data, you identify market gaps, estimate financial metrics, and propose actionable strategies, "
        "all grounded in credible search-based data."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)