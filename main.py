import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.config import settings
from src.views import router as api_router

app = FastAPI()

app.mount("/static", StaticFiles(directory=settings.templates.static_path), name="static")

@app.get("/")
async def index():
    return 1234

app.include_router(
    api_router,
)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)