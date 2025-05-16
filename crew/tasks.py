from crewai import Task
from tools import tool
from agents import news_researcher, news_writer,market_analyst,regional_analyst,country_analyst,strategy_consultant,company_analyst,comprehensive_analyst


# researcher task
#research_task = Task(
#    description=(
#        "Identify the next big trend in {topic}."
#        "Focus on identifying pros and cons and the overall narrative."
#        "Your final report should clearly articulate the key points,"
#        "its market opportunities, and potential risks."
#    ),
#    expected_output="A comprehensive 3000 words long report on the latest AI trends.",
#    tools=[tool],
#    agent=news_researcher
#)
#
## writing task with language model configuration
##write_task = Task(
#    description=(
#        "Compose an insightful article on {topic}."
#        "Focus on the latest trends and how it's impacting the industry."
#        "This article should be easy to understand, engaging, and positive."
#    ),
#    expected_output="A 2000 paragraph article on {topic} advancements formatted as markdown.",
#    tools=[tool],
#    agent=news_writer,
#    async_execution=False,
#    output_file='news.md'
#)



task_market_solution_overview = Task(
        description=(
            "For the problem related to '{topic}', perform the following research:\n"
            "1. Find and report the current estimated market size (e.g., in USD billions, with year if available). Use the search tool to find reliable sources like market research reports or financial news.\n"
            "2. Identify and list existing solutions or approaches addressing this problem. Use the search tool to find company websites, product reviews, and industry articles.\n"
            "3. For these solutions, categorize them into broad types and list any relevant sub-categories. Base this on common industry classifications or logical groupings from your research.\n"
            "4. Provide a detailed summary of these findings, ensuring all information is grounded by search results where possible.\n"
            "Explicitly use the search tool for all data gathering. Be specific and cite sources or provide reasoning for estimations if exact figures aren't available."
            "search for all the products and current distributors/suppliers in india for the product and their contacts and any links "
            "search for the limitation and challenges regarding the current solution"
        ),
        expected_output=(
            "A detailed report including:\n"
             "-I need output in  A4 latex format as a document which i can put in overleaf.com and make it as document"
            "- Estimated market size for '{topic}' (with value, currency, and year, citing source or search query used).\n"
            "- A list of existing solutions- Categories and sub-categories of these solution types, with justification.\n"
             "list all the products and current distributors/suppliers in india for the product and their contacts and any links "
            "list all the limitation and challenges regarding the current solution"
            "- A comprehensive summary of the above points."
            "at least a 2000 word file"
        ),
        agent=market_analyst,
        output_file="1_market_solution_overview.tex"
    )

task_company_market_share = Task(
        description=(
            "Using the previously identified solutions and their categories for '{topic}', analyze the competitive landscape:\n"
            "1. Identify key companies offering these solutions. Use the search tool to find company reports, investor briefings, and industry analyses.\n"
            "2. For each major company, list the specific solutions they offer within the identified categories.\n"
            "3. Estimate or find reported market share for these companies (overall in the '{topic}' market, or for their specific solution categories if possible). Search for 'market share [company name] [topic]' or similar queries.\n"
            "4. If direct market share is unavailable, look for revenue figures attributed to these solutions or companies within the '{topic}' market, or other indicators of market presence (e.g., user base, sales volume from news or reports).\n"
            "Present the findings in a list format: Company Name | Solutions Offered (and their categories) | Estimated Market Share / Revenue (with context/year and source/query).\n"
            "Use the search tool extensively to ground all claims."
            "also specailly do the same tska given on above on india ina saperate section"
        ),
        expected_output=(
            "A report listing key companies in the '{topic}' market, detailing:\n"
             "-I need output in A4 latex format as a document which i can put in overleaf.com and make it as document"

            "- Company Name.\n"
            "- Specific solutions they offer and under which categories these solutions fall.\n"
            "- Estimated market share or revenue generated by these solutions/companies in the '{topic}' market, including any supporting data or source year if found, clearly indicating how this was found via search.\n"
            "The list should be ordered by estimated market share (highest to lowest) if possible, or by significance."
         "at least a 2000 word file"
        ),
        agent=company_analyst,
        context=[task_market_solution_overview],
        output_file="2_company_market_share.tex"
    )

task_continental_analysis = Task(
        description=(
            "Based on the gathered data on solutions for '{topic}' and the companies involved, analyze solution preferences and revenue distribution by continent:\n"
             "-I need output in latex format as a document which i can put in overleaf.com and make it as document"

            "For each major continent (e.g., North America, Europe, Asia, South America, Africa, Oceania):\n"
            "1. Identify which solution types (from Task 1) appear to be most prevalent or preferred. Search for regional market reports, e.g., '[topic] market trends Europe'.\n"
            "2. Estimate the percentage of market preference or adoption for these top solution types within that continent.\n"
            "3. Estimate the approximate revenue generated through these preferred solution types on that continent (e.g., X billion USD). Search for '[topic] market size [continent]'.\n"
            "4. List key companies that are major players for these preferred solution types on that continent.\n"
            "Format: \nCONTINENT NAME\n  Solution Type 1 Preferred: [Estimated % preference/adoption] - Estimated Revenue: [Value Currency] (Source/Query: ...)\n    Companies: [Company A, Company B]\n  Solution Type 2 Preferred: [Estimated % preference/adoption] - Estimated Revenue: [Value Currency] (Source/Query: ...)\n    Companies: [Company C, Company D]\n"
            "Use the search tool to find regional reports, market analyses, or news indicating these preferences and financial estimates, ensuring findings are grounded."
        ),
        expected_output=(
            "A report detailing solution preferences and estimated revenues by continent for the '{topic}' market. For each continent:\n"

             "-I need output in latex A4 format as a document which i can put in overleaf.com and make it as document"
            "- List of preferred solution types with their estimated percentage of adoption/preference and source of this estimation.\n"
            "- Estimated revenue generated by these preferred solution types on the continent, with sources.\n"
            "- Key companies generating revenue through these preferred solutions on the continent, identified via search."
            "-I need output in latex format as a document"
         "at least a 2000 word file"
        ),
        agent=regional_analyst,
        context=[task_market_solution_overview, task_company_market_share],
        output_file="3_continental_solution_preference.tex"
    )

task_country_analysis = Task(
        description=(
            "Perform a similar analysis as Task 3, but focus on the top 20 countries by estimated market size or activity for '{topic}'.\n"
            "First, identify these top 20 countries if not already clear from previous tasks. Use search queries like 'top countries for [topic] market' or '[topic] market size by country'.\n"
            "For each of these top 20 countries:\n"
            "1. Identify which solution types (from Task 1) appear to be most prevalent or preferred. Search e.g., '[topic] solutions [country name]'.\n"
            "2. Estimate the percentage of market preference or adoption for these top solution types within that country.\n"
            "3. Estimate the approximate revenue generated through these preferred solution types in that country.\n"
            "4. List key companies that are major players for these preferred solution types in that country.\n"
            "Format: \nCOUNTRY NAME\n  Solution Type 1 Preferred: [Estimated % preference/adoption] - Estimated Revenue: [Value Currency] (Source/Query: ...)\n    Companies: [Company A, Company B]\n  Solution Type 2 Preferred: [Estimated % preference/adoption] - Estimated Revenue: [Value Currency] (Source/Query: ...)\n    Companies: [Company C, Company D]\n"
            "Use the search tool extensively for country-specific data, ensuring all findings are grounded with search evidence."
        ),
        expected_output=(
             "-I need output in A4 latex format as a document which i can put in overleaf.com and make it as document"
            "A report detailing solution preferences and estimated revenues for the top 20 countries in the '{topic}' market. For each country:\n"
            "- List of preferred solution types with their estimated percentage of adoption/preference, with sources.\n"
            "- Estimated revenue generated by these preferred solution types in the country, with sources.\n"
            "- Key companies generating revenue through these preferred solutions in the country, identified via search."
         "at least a 2000 word file"
        ),
        agent=country_analyst,
        context=[task_market_solution_overview, task_company_market_share, task_continental_analysis],
        output_file="4_country_solution_preference.tex"
    )

task_final_summary_and_suggestion = Task(
        description=(
            "You have now completed a comprehensive multi-stage analysis of the '{topic}' market, grounded with extensive search data. This includes market size, existing solutions and their categories, company market shares, and geographical preferences (continental and top 20 countries).\n"
            "Your final task is to:\n"
            "1. Synthesize and summarize all the key findings from the previous four tasks into a concise executive summary. Reference the grounded data.\n"
            "2. Based on this complete analysis, identify potential gaps, underserved niches, or opportunities in the market. These should be evident from the data collected.\n"
            "3. Propose a strategic solution or market entry approach for a hypothetical new entrant or an existing company looking to expand in the '{topic}' market. Justify your suggestion with data and insights from your analysis. Ensure the suggestion is actionable and specific.\n"
        ),
        expected_output=(
            "A final comprehensive report containing:\n"
             "-I need output in A4 latex format as a document which i can put in overleaf.com and make it as document"

            "1. An Executive Summary of all key findings from the market size, solution types, company shares, continental, and country-level analyses, explicitly referencing the search-grounded data.\n"
            "2. Identification of market gaps, underserved niches, or key opportunities, supported by the data.\n"
            "3. A well-justified strategic solution suggestion or market entry approach for the '{topic}' market, supported by the preceding analysis."
         "at least a 2000 word file"
        ),
        agent=strategy_consultant,
        context=[task_market_solution_overview, task_company_market_share, task_continental_analysis, task_country_analysis],
        output_file="FINAL_Competitor_Analysis_and_Recommendation.tex"
    )




# Single comprehensive task
comprehensive_analysis_task = Task(
    description=(
        "Perform a complete analysis of '{topic}' by executing the following steps, using the search tool for all data gathering:\n\n"
        "1. **Research Breakthroughs**: Identify the latest groundbreaking technologies and trends in '{topic}'. Highlight pros, cons, market opportunities, and risks.\n"
        "2. **Write Narrative**: Compose an engaging, easy-to-understand article on '{topic}', focusing on its latest trends and industry impact.\n"
        "3. **Market Size and Solutions**:\n"
        "   - Estimate the current market size (e.g., USD billions, with year) using market reports or financial news.\n"
        "   - List existing solutions, categorize them into broad types and sub-categories, and justify classifications.\n"
        "4. **Competitive Landscape**:\n"
        "   - Identify key companies and their solutions within the identified categories.\n"
        "   - Estimate market shares or revenues for these companies, using searches like 'market share [company] [topic]' or revenue reports.\n"
        "5. **Continental Analysis**:\n"
        "   - For each continent (North America, Europe, Asia, South America, Africa, Oceania), identify preferred solution types, estimate adoption percentages, "
        "     and approximate revenues. List key companies per continent.\n"
        "6. **Country Analysis**:\n"
        "   - Identify the top 20 countries by market size/activity for '{topic}'.\n"
        "   - For each, list preferred solution types, adoption percentages, revenues, and key companies.\n"
        "7. **Strategic Synthesis**:\n"
        "   - Summarize all findings into an executive summary.\n"
        "   - Identify market gaps, underserved niches, or opportunities.\n"
        "   - Propose a strategic solution or market entry approach for a new/existing player, justified by the analysis.\n\n"
        "All data must be grounded in search results (e.g., market reports, company websites, news). Cite sources or search queries used."
    ),
    expected_output=(
        "A comprehensive LaTeX report in A4 format for Overleaf, including:\n"
        "- **Section 1: Technology Trends**: A 3000-word analysis of breakthroughs, pros, cons, opportunities, and risks in '{topic}'.\n"
        "- **Section 2: Narrative Article**: A 2000-word engaging article on '{topic}' trends and impacts, in markdown embedded in LaTeX.\n"
        "- **Section 3: Market Size and Solutions**: A 2000-word report on market size, solutions, categories, and sub-categories, with sources.\n"
        "- **Section 4: Competitive Landscape**: A 2000-word list of companies, their solutions, categories, and market shares/revenues, with sources.\n"
        "- **Section 5: Continental Analysis**: A 2000-word report on solution preferences, adoption percentages, revenues, and companies per continent.\n"
        "- **Section 6: Country Analysis**: A 2000-word report on preferences, adoption, revenues, and companies for the top 20 countries.\n"
        "- **Section 7: Strategic Recommendations**: A 2000-word executive summary, gap analysis, and strategic proposal, grounded in data.\n"
        "The report must be a single LaTeX file, properly formatted for Overleaf, with citations and at least 14,000 words total."
    ),
    agent=comprehensive_analyst,
    tools=[tool],
    async_execution=False,
    output_file="comprehensive_report.tex"
)