from pydantic import BaseModel


class CreatePost(BaseModel):
    title: str
    text: str
    image_path: str
    title_image: str
    from_title: str

class PostRead(CreatePost):
    pass

class PostUpdate(CreatePost):
    pass