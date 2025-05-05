from typing import Optional

from fastapi import APIRouter, Request, Form, File, UploadFile, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models.dependency import upload_files
from models.schemas import CreatePost
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


@router.get("/create-post")
async def create_post_page(
    request: Request,
):
    return templates.TemplateResponse(request=request, name="make-post.html")


@router.post("/create-post", response_model=None)
async def create_post(
        title: str = Form(...),
        text: str = Form(...),
        image: Optional[UploadFile] = File(None),  # Изменено с image_path
        title_image: Optional[str] = Form(None),  # Сделано необязательным
        from_title: Optional[str] = Form(None),  # Сделано необязательным
        session: AsyncSession = Depends(db_helper.session_dependency),
):
    # Обработка изображения
    image_path = None
    if image:
        image_path = await upload_files(image)  # Предполагается, что upload_files обрабатывает UploadFile

    post_in = CreatePost(
        title=title,
        text=text,
        image_path=image_path,  # Может быть None
        title_image=title_image,  # Может быть None
        from_title=from_title,  # Может быть None
    )

    try:
        post = await TaskRepository.create_post(session=session, post=post_in)
        return post
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
