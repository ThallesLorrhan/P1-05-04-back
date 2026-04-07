from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class GeneroEnum(str, Enum):
    ficcao = "Ficção"
    romance = "Romance"
    terror = "Terror"
    ciencia = "Ciência"
    historia = "História"
    fantasia = "Fantasia"
    biografia = "Biografia"
    outro = "Outro"

class LivroCreate(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=200, description="Título do livro")
    autor: str = Field(..., min_length=1, max_length=150, description="Nome do autor")
    ano_publicacao: int = Field(..., ge=1000, le=2100, description="Ano de publicação")
    genero: GeneroEnum = Field(..., description="Gênero literário")

    class Config:
        json_schema_extra = {
            "example": {
                "titulo": "O Senhor dos Anéis",
                "autor": "J.R.R. Tolkien",
                "ano_publicacao": 1954,
                "genero": "Fantasia"
            }
        }

class LivroUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=1, max_length=200)
    autor: Optional[str] = Field(None, min_length=1, max_length=150)
    ano_publicacao: Optional[int] = Field(None, ge=1000, le=2100)
    genero: Optional[GeneroEnum] = None

class LivroResponse(BaseModel):
    id: str
    titulo: str
    autor: str
    ano_publicacao: int
    genero: str
