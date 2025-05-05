import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from src.config import settings
from src.views import router as api_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Для разработки можно "*", для продакшена укажите конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=settings.templates.static_path), name="static")

@app.get("/")
async def index():
    return 1234

app.include_router(
    api_router,
)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)