from agents.base_agent import create_assistant
from tools.job_api import search_jobs

job_search_agent = create_assistant(
    name="JobSearchAgent",
    system_message="Use tool to search relevant jobs only.",
    function_map={"search_jobs": search_jobs}
)
