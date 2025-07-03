import os
import requests
from dotenv import load_dotenv

load_dotenv()
YOUR_API_KEY = os.getenv("API_KEY")

def generate_readme_from_repo(repo_info):
    prompt = f"""
Generate a professional and comprehensive README.md file in GitHub Markdown format for the following repository. The README must include:

1. Project Title (as a top-level heading)
2. Description (brief overview of the project)
3. Table of Contents (with links to each section)
4. Technologies Used (list all major frameworks, libraries, and tools)
5. Requirements (list all prerequisites and dependencies)
6. Installation Instructions (step-by-step guide to set up the project)
7. Usage Instructions (how to use or run the project, with code examples if possible)
8. Contribution Guidelines (how others can contribute)
9. License Information (include the license type and a short note)

Use the following repository details:

- Project Name: {repo_info['name']}
- Description: {repo_info['description']}
- Primary Language: {repo_info['language']}
- Topics: {', '.join(repo_info['topics'])}
- Repository URL: {repo_info['url']}

Add relevant badges and ensure the README is well-structured and easy to navigate.
    """

    response = requests.post(
        "https://api.perplexity.ai/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "model",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
    )
    return response.json()['choices'][0]['message']['content']
