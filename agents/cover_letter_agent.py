from agents.base_agent import create_assistant

cover_letter_agent = create_assistant(
    name="CoverLetterAgent",
    system_message="""
    Generate a personalized cover letter tailored to job description.
    Professional and concise.
    """
)
