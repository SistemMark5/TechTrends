from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class Post(Base):
    __tablename__ = "posts"

    title: Mapped[str]
    text: Mapped[str] = mapped_column(Text)
    image_path: Mapped[str]
    title_image: Mapped[str]
    from_title: Mapped[str]