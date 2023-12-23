from sqlalchemy import Column, Integer, String, ForeignKey,relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    name: str = Column(String)
    email: str = Column(String)
    password: str = Column(String)
    todos = relationship("TODO", back_populates="owner", cascade="all, delete-orphan")

