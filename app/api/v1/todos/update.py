# app/api/v1/todos/update.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.todo import TodoUpdate
from app.schemas.todo import Todo as TodoResponse
from app.models.todo import Todo
from datetime import datetime

router = APIRouter()

@router.put("/todos/{id}", response_model=TodoResponse)
async def update_todo(
    id: int, todo: TodoUpdate, db: Session = Depends(get_db)
):
    """
    Update a todo.
    """
    db_todo = db.query(Todo).filter(Todo.id == id).first()

    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    for field, value in todo.dict(exclude_unset=True).items():
        setattr(db_todo, field, value)

    db_todo.updated_at = datetime.now()

    db.commit()
    db.refresh(db_todo)

    return db_todo