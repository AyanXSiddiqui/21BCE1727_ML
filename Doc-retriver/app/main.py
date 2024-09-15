from fastapi import FastAPI
from .api.endpoints import health_check, document_search

app = FastAPI(title="Document Retrieval System")

app.include_router(health_check.router)
app.include_router(document_search.router)
