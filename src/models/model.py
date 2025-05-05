from datetime import datetime

from sqlalchemy import Text, func
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class Post(Base):
    __tablename__ = "posts"

    title: Mapped[str]
    text: Mapped[str] = mapped_column(Text)
    image_path: Mapped[str]
    title_image: Mapped[str]
    from_title: Mapped[str]
    date_post: Mapped[datetime] = mapped_column(server_default=func.now())