def extract_skills(resume_text: str, github_data: dict):
    skill_keywords = [
        "python", "javascript", "react", "html", "css", "fastapi",
        "django", "flask", "sql", "mongodb", "git", "docker", "rest api"
    ]

    resume_text = resume_text.lower()
    resume_skills = {skill: (skill in resume_text) for skill in skill_keywords}

   
    lang_map = {
        "python": "python",
        "javascript": "javascript",
        "html": "html",
        "css": "css",
        "typescript": "javascript",
        "dockerfile": "docker",
        "sql": "sql",
    }

    github_skills = {skill: 0 for skill in skill_keywords}
    for lang, count in github_data.get("languages", {}).items():
        lang_lower = lang.lower()
        mapped = lang_map.get(lang_lower)
        if mapped:
            github_skills[mapped] += count

    
    skill_map = {}
    for skill in skill_keywords:
        skill_map[skill] = {
            "resume": resume_skills.get(skill, False),
            "github": github_skills.get(skill, 0)
        }

    return skill_map