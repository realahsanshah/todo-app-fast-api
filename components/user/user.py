from fastapi import APIRouter, Depends, HTTPException
from dto.user import UserCreate
from sqlalchemy.orm import Session
from database import get_db
from models.user import User

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

def create_user(db:Session,current_user=UserCreate):
    user = User(email=current_user.email,name=current_user.name,password=current_user.password)
    
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db:Session,email:str):
    user = db.query(User).filter(User.email == email).first()
    return user

@router.post("/signup")
def signup(user_data:UserCreate,db: Session = Depends(get_db)):
    user = get_user(db=db,email=user_data.email)

    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    signup_user = create_user(db=db,current_user=user_data) 
    return signup_user

