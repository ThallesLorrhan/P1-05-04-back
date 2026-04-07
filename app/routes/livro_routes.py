from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.livro_schema import LivroCreate, LivroUpdate, LivroResponse
from app.repositories import livro_repository as repo

router = APIRouter()

@router.post(
    "/",
    response_model=LivroResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Criar um novo livro"
)
async def create_livro(livro: LivroCreate):
    created = await repo.create_livro(livro)
    return created

@router.get(
    "/",
    response_model=List[LivroResponse],
    summary="Listar todos os livros"
)
async def list_livros():
    return await repo.get_all_livros()

@router.get(
    "/{livro_id}",
    response_model=LivroResponse,
    summary="Buscar livro por ID"
)
async def get_livro(livro_id: str):
    livro = await repo.get_livro_by_id(livro_id)
    if not livro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Livro com id '{livro_id}' não encontrado"
        )
    return livro

@router.put(
    "/{livro_id}",
    response_model=LivroResponse,
    summary="Atualizar livro por ID"
)
async def update_livro(livro_id: str, livro: LivroUpdate):
    updated = await repo.update_livro(livro_id, livro)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Livro com id '{livro_id}' não encontrado"
        )
    return updated

@router.delete(
    "/{livro_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deletar livro por ID"
)
async def delete_livro(livro_id: str):
    deleted = await repo.delete_livro(livro_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Livro com id '{livro_id}' não encontrado"
        )
