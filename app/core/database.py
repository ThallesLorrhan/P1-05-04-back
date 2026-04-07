import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017")
DB_NAME = os.getenv("DB_NAME", "livros_db")

class Database:
    client: AsyncIOMotorClient = None
    db = None

db = Database()

async def connect_db():
    db.client = AsyncIOMotorClient(MONGO_URL)
    db.db = db.client[DB_NAME]
    print(f"Conectado ao MongoDB: {MONGO_URL}/{DB_NAME}")

async def close_db():
    if db.client:
        db.client.close()
        print("Conexão com MongoDB encerrada")

def get_db():
    return db.db
