import os
from fastapi import FastAPI
from components.todo.todo import router as todo_router
from components.user.user import router as user_router

# print(os.environ['SQLALCHEMY_DATABASE_URL'])
app = FastAPI()


app.include_router(
    user_router, prefix="",tags=["user"]
)   

app.include_router(
    todo_router, prefix="",tags=["todo"]
)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("app", host="127.0.0.1", port=8000,reload=True)