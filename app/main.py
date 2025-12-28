from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.github import router as github_router
from app.routes.resume import router as resume_router
from app.routes.skills import router as skills_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(github_router)
app.include_router(resume_router)
app.include_router(skills_router)

@app.get("/")
def root():
    return {"status": "SkillSignal API running"}