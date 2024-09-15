from pydantic import BaseModel

class DocumentBase(BaseModel):
    text: str

class DocumentCreate(DocumentBase):
    pass

class Document(DocumentBase):
    id: int

    class Config:
        orm_mode = True
