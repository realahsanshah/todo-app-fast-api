# app/models/todo.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from app.database.base_class import Base

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(120), index=True, )
    description = Column(String(255), index=True, nullable=True)
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    def __str__(self):
        return f"Todo #{self.id}: {self.title}, Completed: {self.is_completed}"