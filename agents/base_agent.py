import autogen
from config.llm_config import get_llm_config

def create_assistant(name, system_message, function_map=None):
    return autogen.AssistantAgent(
        name=name,
        llm_config=get_llm_config(),
        system_message=system_message,
        function_map=function_map
    )
