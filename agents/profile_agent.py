from agents.base_agent import create_assistant

profile_agent = create_assistant(
    name="ProfileAgent",
    system_message="""
    Extract:
    - skills
    - experience
    - preferred role
    - location preference
    Return structured summary.
    """
)
