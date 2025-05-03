from fastapi import Path, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.annotation import Annotated

from src.db_helper import db_helper
from src.models.repository import TaskRepository


async def get_by_title(title: Annotated[str, Path], session: AsyncSession = Depends(db_helper.session_dependency)):
    response = TaskRepository.get_post_by_title(title=title, session=session)
    if response is not None:
        return response

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND
    )