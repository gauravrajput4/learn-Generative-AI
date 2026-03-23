from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id:int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str]=[]

    model_config = ConfigDict(
        json_encoders={
            datetime:lambda v:v.strftime("%d/%m/%Y %H:%M:%S %p")
        }
    )

user=User(
    id=1,
    name="Gaurav",
    email="mrgauravrajput4@gmail.com",
    created_at=datetime(2026,3,23,4,26),
    address=Address(
        street="Street 1",
        city="Mohali",
        postal_code="140307"
    ),
    tags=["Software Development","Gen AI"],
)

user_dict=user.model_dump()
print("Dictionary Representation:",user_dict)

json_user=user.model_dump_json()
print("JSON Representation:",json_user)
