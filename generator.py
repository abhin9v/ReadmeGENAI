import os
import requests
from dotenv import load_dotenv

load_dotenv()
PPLX_API_KEY = os.getenv("PPLX_API_KEY")

def generate_readme_from_repo(repo_info):
    prompt = f"""
Generate a professional README.md file in GitHub Markdown format using the following repository details:

- Project Name: {repo_info['name']}
- Description: {repo_info['description']}
- Primary Language: {repo_info['language']}
- Topics: {', '.join(repo_info['topics'])}
- Repository URL: {repo_info['url']}

Include sections like Description, Features, Installation, Usage, Technologies Used, and License. Add relevant badges.
    """

    response = requests.post(
        "https://api.perplexity.ai/chat/completions",
        headers={
            "Authorization": f"Bearer {PPLX_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "sonar-pro",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
    )
    return response.json()['choices'][0]['message']['content']
