from pydantic import BaseModel
from typing import List,Dict,Optional

class Cart(BaseModel):
    user_id:int
    items: List[str]
    quantity:Dict[str,int]

class BlogPost(BaseModel):
    title: str
    content: str
    image_url:Optional[str] = None

cart_data={
    'user_id':1,
    'items':[
        "Laptop",
        "MacBook",
        "Smartphone",
        "Keyboard"
    ],
    'quantity':{
        'Laptop':1,
        'MacBook':1,
        'Smartphone':1,
        'Keyboard':3
    }
}

cart=Cart(**cart_data)
print(cart)