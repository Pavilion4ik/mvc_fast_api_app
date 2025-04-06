from pydantic import BaseModel


class Token(BaseModel):
    """
    Schema for the token (JWT) response after login or signup.
    """

    access_token: str
    token_type: str = "bearer"

    class Config:
        from_attributes = True
