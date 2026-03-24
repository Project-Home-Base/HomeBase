from fastapi import FastAPI
from identity import router as identity_router
from metadata import router as metadata_router
from storage import router as storage_router

app = FastAPI(title="HomeBase Local Cloud API")

app.include_router(identity_router, prefix="/api/identity", tags=["identity"])
app.include_router(metadata_router, prefix="/api/metadata", tags=["metadata"])
app.include_router(storage_router, prefix="/api/storage", tags=["storage"])

@app.get("/health")
def health_check():
    return {"status": "ok"}
