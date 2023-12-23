from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base,relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name: str = Column(String)
    email: str = Column(String)
    password: str = Column(String)
    todos = relationship('Todo', back_populates="owner", cascade="all, delete-orphan")

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    is_completed = Column(Integer)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner=relationship("User", back_populates="todos")
