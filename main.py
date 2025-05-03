import uvicorn
from fastapi import FastAPI
from src.views import router as api_router

app = FastAPI()

@app.get("/")
async def index():
    return 1234

app.include_router(
    api_router,
)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)