from typing import List,Optional
from pydantic import  BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

address=Address(
    street="Street 1",
    city="Mohali",
    postal_code="140307"
)

user1 = User(
    id=123,
    name="Gaurav",
    address=address
)


user_data={
    "id":456,
    "name":"Gaurav Rajput",
    "address":{
        "street":"Street 2",
        "city":"Mohali",
        "postal_code":"140307"
    }
}

user2=User(**user_data)
print(user1)
print(user2)