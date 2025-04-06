from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    """
    Base schema for User.
    Used for common user information (email, etc.)
    """
    email: EmailStr

class UserCreate(UserBase):
    """
    Schema for creating a new user.
    Inherits from UserBase and adds password field.
    """
    password: str

    class Config:
        from_attributes = True

class UserResponse(UserBase):
    """
    Schema for user response (login, etc.)
    """
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
