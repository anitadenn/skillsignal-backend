import requests

def analyze_github(username: str):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "GitHub user not found"}

    repos = response.json()
    languages = {}

    for repo in repos:
        lang = repo.get("language")
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

    return {
        "repo_count": len(repos),
        "languages": languages
    }