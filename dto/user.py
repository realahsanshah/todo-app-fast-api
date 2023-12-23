from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
   email: EmailStr

class UserCreate(UserBase):
   name: str
   password: str