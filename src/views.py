from fastapi import APIRouter, Request

from utils.templates import templates

router = APIRouter(prefix="/news")

@router.get("")
async def news_page(
        request: Request
):
    return templates.TemplateResponse(
        request=request,
        name="news.html",
    )