import uvicorn
from fastapi import FastAPI
from app.api.routes import router
from contextlib import asynccontextmanager
from storage.db_handler import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield  

app = FastAPI(
    title="IA Movie Insights",
    description="🚀 API com OpenAI que retorna informações sobre filmes com base no título.",
    version="1.0.0",
    lifespan=lifespan  
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)