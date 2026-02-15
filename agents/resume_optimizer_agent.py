from agents.base_agent import create_assistant

resume_optimizer_agent = create_assistant(
    name="ResumeOptimizerAgent",
    system_message="""
    Improve resume bullet points based on job description.
    Make it ATS-friendly.
    """
)
