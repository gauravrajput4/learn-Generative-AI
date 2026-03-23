from pydantic import BaseModel, field_validator, model_validator
from typing import Optional

class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls,value):
        if len(value) < 4:
            raise ValueError("Username must be at least 4 characters long")
        return value

class SignUp(BaseModel):
    username: str
    email: str
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_is_valid(cls,values):
        if values.password != values.confirm_password:
            raise ValueError("Passwords don't match")
        return values
