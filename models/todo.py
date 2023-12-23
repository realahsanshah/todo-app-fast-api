from sqlalchemy import Column, Integer, String, ForeignKey,relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    is_completed = Column(Integer)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner=relationship("User", back_populates="todos")

