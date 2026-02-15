import autogen

from agents.profile_agent import profile_agent
from agents.job_search_agent import job_search_agent
from agents.resume_optimizer_agent import resume_optimizer_agent
from agents.cover_letter_agent import cover_letter_agent
from config.llm_config import get_llm_config


executor = autogen.UserProxyAgent(
    name="Executor",
    code_execution_config=False,
    human_input_mode="NEVER"  # Fully Autonomous. No Human input needed
)

groupchat = autogen.GroupChat(
    agents=[
        profile_agent,
        job_search_agent,
        resume_optimizer_agent,
        cover_letter_agent,
        executor
    ],
    messages=[],
    max_round=5,
    speaker_selection_method="round_robin"
)

manager = autogen.GroupChatManager(
    groupchat=groupchat,
    llm_config=get_llm_config()   # LLM Config
)


def run_job_search(user_prompt):
    return executor.initiate_chat(
        manager,
        message=user_prompt
    )
