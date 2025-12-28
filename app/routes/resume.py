from fastapi import APIRouter, UploadFile, File
import shutil
from app.services.resume_parser import parse_resume

router = APIRouter()

@router.post("/resume")
def upload_resume(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = parse_resume(file_path)
    return {"extracted_text": text[:1000]}