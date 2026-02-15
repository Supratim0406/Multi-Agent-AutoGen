import os
from dotenv import load_dotenv

load_dotenv()

# def get_llm_config():
#     return {
#         "config_list": [
#             {
#                 "model": "llama-3.3-70b-versatile",
#                 "api_key": os.getenv("GROQ_API_KEY"),
#                 "base_url": "https://api.groq.com/openai/v1",  # REQUIRED as GROQ uses this
#                 "price": [0.0, 0.0], # To Stop price warning from GROQ
#             }
#         ],
#         "temperature": 0.3
#     }

def get_llm_config():
    return {
        "config_list": [
            {
                "model": "mistral:latest",  # Must match ollama list
                "base_url": "http://localhost:11434/v1",
                "api_key": "ollama",  # dummy value (required but ignored)
                "price": [0.0, 0.0],
            }
        ],
        "temperature": 0.3,
    }