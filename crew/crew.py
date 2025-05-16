from crewai import Crew, Process
from tasks import task_company_market_share,task_continental_analysis,task_country_analysis,task_final_summary_and_suggestion,task_market_solution_overview
from agents import strategy_consultant,company_analyst,regional_analyst,country_analyst,market_analyst
from agents import comprehensive_analyst
from tasks import  comprehensive_analysis_task

# forming the tech focused crew with some enhanced configuration
crew = Crew(
    agents=[market_analyst,company_analyst,regional_analyst,country_analyst,strategy_consultant,],
    tasks=[task_market_solution_overview,task_company_market_share,task_continental_analysis,task_country_analysis,task_final_summary_and_suggestion,],
    process=Process.sequential,
)

# starting the task execution process with enhanced feedback

result = crew.kickoff(inputs={'topic': 'At home fertility tests'})
print(result)