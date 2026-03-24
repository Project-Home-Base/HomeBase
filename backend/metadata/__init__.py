from fastapi import APIRouter

router = APIRouter()

@router.get("/directories")
def list_directories(parent_id: str | None = None):
    return {"message": "Not implemented"}

@router.post("/directories")
def create_directory(name: str, parent_id: str | None = None):
    return {"message": "Not implemented"}

@router.get("/files")
def list_files(directory_id: str):
    return {"message": "Not implemented"}
