
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dto.todo import TODOCreate

router = APIRouter(
    prefix="/todo",
    tags=["todo"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create-dto")
def create_todo(text: str,completed: bool=False,):
    try:
        todo = TODOCreate(text=text,completed=completed)
        Session.add(todo)
        Session.commit()
        return {
            "message": "Todo created successfully",
            "data": todo
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    


