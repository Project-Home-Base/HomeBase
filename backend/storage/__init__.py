from fastapi import APIRouter

router = APIRouter()

@router.post("/upload")
def upload_file():
    return {"message": "Not implemented"}

@router.get("/download/{file_id}")
def download_file(file_id: str):
    return {"message": "Not implemented"}
