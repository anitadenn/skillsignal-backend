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
        resume_found = resume_skills.get(skill, False)
        github_value = github_skills.get(skill, 0)

        # Resume weight
        resume_score = 40 if resume_found else 0

        # GitHub weight (normalized)
        github_score = int((github_value / max_github) * 60) if github_value else 0

        total_score = min(resume_score + github_score, 100)

        skill_map[skill] = {
            "score": total_score,
            "resume": resume_found,
            "github": github_value
        }


    return skill_map