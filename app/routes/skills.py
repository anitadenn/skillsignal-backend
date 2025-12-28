from fastapi import APIRouter, UploadFile, File, Form
from app.services.resume_parser import parse_resume
from app.services.github_analyzer import analyze_github
from app.services.skill_extractor import extract_skills
import shutil

router = APIRouter()

@router.post("/analyze")
def analyze_skills(
    github_username: str = Form(...),
    resume_file: UploadFile = File(...)
):
    # Save uploaded resume to a temporary file
    file_path = f"temp_{resume_file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume_file.file, buffer)

    # Extract text from resume
    resume_text = parse_resume(file_path)

    # Fetch GitHub data
    github_data = analyze_github(github_username)

    # Generate skill map
    skill_map = extract_skills(resume_text, github_data)

    return {
        "github_data": github_data,
        "skill_map": skill_map
    }