from fastapi import FastAPI
from agents.manager import run_job_search

app = FastAPI()

@app.post("/search")
def search(payload: dict):
    try:
        result = run_job_search(payload["query"])

        if hasattr(result, "summary") and result.summary:
            final_answer = result.summary
        else:
            final_answer = result.chat_history[-1]["content"]

        return {"result": final_answer}

    except Exception as e:
        return {"error": str(e)}
