from fastapi import APIRouter
from app.services.github_analyzer import analyze_github

router = APIRouter()

@router.get("/github/{username}")
def github_analysis(username: str):
    return analyze_github(username)