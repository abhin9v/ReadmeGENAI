import requests

def fetch_repo_data(github_url):
    # Parse user and repo from URL
    parts = github_url.rstrip("/").split("/")
    owner, repo = parts[-2], parts[-1]

    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(api_url)
    if response.status_code != 200:
        return None

    repo_data = response.json()
    return {
        "name": repo_data.get("name", ""),
        "description": repo_data.get("description", ""),
        "topics": repo_data.get("topics", []),
        "language": repo_data.get("language", ""),
        "owner": repo_data.get("owner", {}).get("login", ""),
        "url": repo_data.get("html_url", github_url)
    }
