import os.path
from datetime import datetime

from fastapi import Path, HTTPException, status, Form, File, UploadFile
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.annotation import Annotated

from src.config import settings
from src.models.db_helper import db_helper
from src.models.crud import TaskRepository


async def get_by_title(title: Annotated[str, Path], session: AsyncSession = Depends(db_helper.session_dependency)):
    response = TaskRepository.get_post_by_title(title=title, session=session)
    if response is not None:
        return response

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND
    )


async def upload_files(file: UploadFile):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_filename = f"{timestamp}_{file.filename}"
    file_path = os.path.join(settings.files.file_dir, new_filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    return str(file_path)