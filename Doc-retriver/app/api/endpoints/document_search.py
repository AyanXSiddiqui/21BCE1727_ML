from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas, database

router = APIRouter()

@router.post("/search", response_model=list[schemas.Document])
def search_documents(text: str, db: Session = Depends(database.SessionLocal)):
    documents = crud.search_documents_by_text(db, text=text)
    if not documents:
        raise HTTPException(status_code=404, detail="Document not found")
    return documents
