from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login():
    return {"message": "Not implemented"}

@router.get("/me")
def get_current_user():
    return {"message": "Not implemented"}
