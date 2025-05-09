from pydantic import BaseModel, ConfigDict


class CreatePost(BaseModel):
    title: str
    text: str | None
    image_path: str | None = "img/default.jpg"
    title_image: str | None
    from_title: str | None

class PostRead(CreatePost):
    pass

class PostUpdate(CreatePost):
    pass

class AddPost(CreatePost):
    id: int

    model_config = ConfigDict(from_attributes=True)