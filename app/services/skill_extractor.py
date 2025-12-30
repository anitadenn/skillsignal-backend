def extract_skills(resume_text: str, github_data: dict):
    skill_keywords = [
        "python", "javascript", "react", "html", "css", "fastapi",
        "django", "flask", "sql", "mongodb", "git", "docker", "rest api"
    ]

    resume_text = resume_text.lower()

    # 1. Resume detection
    resume_skills = {skill: (skill in resume_text) for skill in skill_keywords}

    # 2. GitHub language mapping
    lang_map = {
        "python": "python",
        "javascript": "javascript",
        "typescript": "javascript",
        "html": "html",
        "css": "css",
        "dockerfile": "docker",
        "sql": "sql",
    }

    github_skills = {skill: 0 for skill in skill_keywords}

    for lang, count in github_data.get("languages", {}).items():
        lang_lower = lang.lower()
        mapped = lang_map.get(lang_lower)
        if mapped:
            github_skills[mapped] += count

    # 3. Normalize GitHub scores
    max_github = max(github_skills.values(), default=1)

    skill_map = {}

    for skill in skill_keywords:
        score = 0

        # Resume weight
        if resume_skills.get(skill):
            score += 40

        # GitHub weight
        github_value = github_skills.get(skill, 0)
        github_score = int((github_value / max_github) * 60) if github_value else 0
        score += github_score

        skill_map[skill] = min(score, 100)

    return skill_map