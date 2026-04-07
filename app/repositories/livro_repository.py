from bson import ObjectId
from bson.errors import InvalidId
from typing import List, Optional
from app.core.database import get_db
from app.models.livro_model import LivroModel
from app.schemas.livro_schema import LivroCreate, LivroUpdate

COLLECTION = "livros"

async def create_livro(data: LivroCreate) -> dict:
    db = get_db()
    livro_dict = data.model_dump()
    result = await db[COLLECTION].insert_one(livro_dict)
    created = await db[COLLECTION].find_one({"_id": result.inserted_id})
    return LivroModel.from_mongo(created)

async def get_all_livros() -> List[dict]:
    db = get_db()
    livros = []
    async for doc in db[COLLECTION].find():
        livros.append(LivroModel.from_mongo(doc))
    return livros

async def get_livro_by_id(livro_id: str) -> Optional[dict]:
    db = get_db()
    try:
        oid = ObjectId(livro_id)
    except InvalidId:
        return None
    doc = await db[COLLECTION].find_one({"_id": oid})
    return LivroModel.from_mongo(doc) if doc else None

async def update_livro(livro_id: str, data: LivroUpdate) -> Optional[dict]:
    db = get_db()
    try:
        oid = ObjectId(livro_id)
    except InvalidId:
        return None
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    if not update_data:
        return await get_livro_by_id(livro_id)
    await db[COLLECTION].update_one({"_id": oid}, {"$set": update_data})
    updated = await db[COLLECTION].find_one({"_id": oid})
    return LivroModel.from_mongo(updated) if updated else None

async def delete_livro(livro_id: str) -> bool:
    db = get_db()
    try:
        oid = ObjectId(livro_id)
    except InvalidId:
        return False
    result = await db[COLLECTION].delete_one({"_id": oid})
    return result.deleted_count == 1
