from pydantic import BaseModel
from typing import Optional,List

class Comment(BaseModel):
    id: int
    message: str
    replies:Optional[List['Comment']]=None

Comment.model_rebuild()

comment = Comment(
    id=123,
    message="First comment",
    replies=[
        Comment(
            id=456,
            message="Second comment",
        ),
        Comment(
            id=789,
            message="Third comment",
        )
    ]
)
print(comment)