from fastapi import APIRouter, Request
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.datastructures import UploadFile

from src.models.crud import TaskRepository
from src.models.db_helper import db_helper
from src.utils.templates import templates

router = APIRouter(prefix="/news")

@router.get("/")
async def news_page(
        request: Request,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    posts = await TaskRepository.get_posts(session=session)

    return templates.TemplateResponse(
        request=request,
        name="news.html",
        context={"posts": posts}
    )

@router.get("/create-post")
async def create_post_page(
        request: Request,
):
    return templates.TemplateResponse(
        request=request,
        name="make-post.html"
    )

@router.post("/create-post")
async def create_post(
        request: Request,
):
    pass