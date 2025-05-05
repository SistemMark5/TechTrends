from http.client import responses
from typing import Annotated

from fastapi import APIRouter, Request, Form
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import RedirectResponse

from models.dependency import upload_files
from models.schemas import CreatePost, AddPost
from src.models.crud import TaskRepository
from src.models.db_helper import db_helper
from src.utils.templates import templates

router = APIRouter(prefix="/news")


@router.get("/", response_model=None)
async def news_page(
    request: Request, session: AsyncSession = Depends(db_helper.session_dependency)
):
    posts = await TaskRepository.get_posts(session=session)

    return templates.TemplateResponse(
        request=request, name="news.html", context={"posts": posts}
    )


@router.get("/create-post", response_model=None)
async def create_post_page(
    request: Request,
):
    return templates.TemplateResponse(request=request, name="make-post.html")


@router.post("/create-post", response_model=None)
async def create_post(
    request: Request,
    title: str = Form(...),
    text: str = Form(...),
    image_path: str | None = Depends(upload_files),
    title_image: str = Form(...),
    from_title: str = Form(...),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    post_in = CreatePost(
        title=title,
        text=text,
        image_path=image_path,
        title_image=title_image,
        from_title=from_title,
    ).model_validate()
    post = await TaskRepository.create_post(session=session, post=post_in)
    return RedirectResponse(url="/create-post", status_code=303)
