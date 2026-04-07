from bson import ObjectId
from typing import Optional

class LivroModel:
    """Representação do documento Livro no MongoDB"""

    @staticmethod
    def from_mongo(document: dict) -> dict:
        """Converte documento MongoDB para dict com id como string"""
        if document is None:
            return None
        document["id"] = str(document.pop("_id"))
        return document

    @staticmethod
    def to_mongo(data: dict) -> dict:
        """Prepara dict para inserção no MongoDB"""
        if "id" in data:
            data["_id"] = ObjectId(data.pop("id"))
        return data
