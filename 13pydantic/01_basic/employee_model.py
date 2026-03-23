from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=30,
        description="The employees Name",
        example="Gaurav"
    )
    department: Optional[str]='General'
    salary: float=Field(
        ...,
        ge=10000,
        le=1000000,
        description="The employee salary",
        example=20000
    )


class User(BaseModel):
    email:str=Field(
        ...,
        regex=r''
    )
    phone:str=Field(
        ...,
        regex=r''
    )
    age:int=Field(
        ...,
        ge=0,
        le=150,
        description="The employee age",
    )
    discount:float=Field(
        ...,
        ge=0,
        le=100,
        description="The employee discount",
    )