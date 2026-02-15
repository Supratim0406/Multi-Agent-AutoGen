import requests
import os

def search_jobs(query, location):
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google_jobs",
        "q": query,
        "location": location,
        "api_key": os.getenv("SERPAPI_KEY")
    }
    r = requests.get(url, params=params).json()

    jobs = []
    for job in r.get("jobs_results", [])[:10]:
        jobs.append({
            "title": job["title"],
            "company": job["company_name"],
            "location": job["location"],
            "description": job["description"]
        })

    return jobs
