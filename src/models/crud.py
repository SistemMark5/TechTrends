from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.model import Post
from src.models.schemas import CreatePost, PostUpdate, AddPost


class TaskRepository:

    @classmethod
    async def create_post(cls, post: CreatePost, session: AsyncSession) -> None:
        task_dict = post.model_dump()
        task = Post(**task_dict)
        session.add(task)
        await session.commit()

    @classmethod
    async def get_posts(cls, session: AsyncSession) -> Post:
        stmt = select(Post)
        result = await session.execute(stmt)
        posts = result.scalars().all()
        return posts

    @classmethod
    async def update_post(cls, session: AsyncSession, post_in: AddPost, post_update: PostUpdate) -> None:
        for key, value in post_update.model_dump().items():
            setattr(post_in, key, value)
        await session.commit()

    @classmethod
    async def get_post_by_title(cls, session: AsyncSession, title: str):
        stmt = select(Post).filter(Post.title == title)
        result = await session.execute(stmt)
        post_by_title = result.scalars().first()
        return post_by_title

    @classmethod
    async def delete_post(cls, session: AsyncSession, post: AddPost) -> None:
        await session.delete(post)
        await session.commit()