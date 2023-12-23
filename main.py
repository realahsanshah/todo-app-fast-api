import os
from fastapi import FastAPI
from components.todo.todo import router

# print(os.environ['SQLALCHEMY_DATABASE_URL'])
app = FastAPI()


app.include_router(
    router, prefix="",tags=["todo"]
)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("app", host="127.0.0.1", port=8000,reload=True)