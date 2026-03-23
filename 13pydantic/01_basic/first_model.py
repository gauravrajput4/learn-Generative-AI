from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {
    'id':101,
    'name':'Gaurav',
    'is_active':True
}

user=User(**input_data) #Always unpack the dictionary when creating an instance of the model



print(user)