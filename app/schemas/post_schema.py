from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, constr


class PostBase(BaseModel):
    """
    Base schema for Post.
    Contains the common fields (text).
    """

    text: constr(min_length=1, max_length=1000)


class PostCreate(PostBase):
    """
    Schema for creating a new post.
    Inherits from PostBase and validates text field.
    """

    class Config:
        from_attributes = True


class PostResponse(PostBase):
    """
    Schema for post response when fetching posts.
    Contains the post id and creation date.
    """

    id: int
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True


class PostListResponse(BaseModel):
    """
    Schema for listing posts (response).
    Contains a list of posts.
    """

    posts: List[PostResponse]

    class Config:
        from_attributes = True
