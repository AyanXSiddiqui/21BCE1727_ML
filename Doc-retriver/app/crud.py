from sqlalchemy.orm import Session
from . import models, schemas

def get_document(db: Session, document_id: int):
    return db.query(models.Document).filter(models.Document.id == document_id).first()

def create_document(db: Session, document: schemas.DocumentCreate):
    db_document = models.Document(text=document.text)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document
