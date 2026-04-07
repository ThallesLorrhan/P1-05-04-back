from fastapi import FastAPI
from app.core.database import connect_db, close_db
from app.routes.livro_routes import router as livro_router

app = FastAPI(
    title="CRUD de Livros",
    description="API REST para gerenciamento de livros usando FastAPI e MongoDB",
    version="1.0.0"
)

@app.on_event("startup")
async def startup():
    await connect_db()

@app.on_event("shutdown")
async def shutdown():
    await close_db()

app.include_router(livro_router, prefix="/livros", tags=["Livros"])

@app.get("/")
async def root():
    return {"message": "API de Livros - CRUD com FastAPI e MongoDB"}
