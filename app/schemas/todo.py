from pydantic import BaseModel
from datetime import datetime

class TodoBase(BaseModel):
    title:str
    description:str = None
    is_completed:bool = False


class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    title:str = None
    description:str = None
    is_completed:bool = False

class Todo(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True