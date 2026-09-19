from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Get requests
@app.get('/')
def home():
    return {"message": "TaskFlow API is running"}


# @app.get('/health')
# def health():
#     return {"status": "healthy"}


# @app.get('/users')
# def users():
#     return {"users": [{"name": "mouse"}, {"name": "cat"}]}


@app.get('/tasks')
def tasks():
    return {"tasks": tasks}


# Path parameters
# /tasks/2

# # Get /tasks/1
# @app.get('/tasks/{task_id}')
# def get_task(task_id: int):
#     tasks_list = {
#         "tasks": [
#             {"task1": "learn fastapi"},
#             {"task2": "learn react"},
#             {"task3": "learn postgresql"}
#         ]
#     }
#     return {"task_id": tasks_list["tasks"][task_id]}

# # Get /users/mouse


# @app.get('/users/{user_name}')
# def get_user(user_name: str):
#     users_list = {
#         "users": [{"name": "mouse", "age": 23}, {"name": "cat", "age": 19}]}
#     user_to_get = ''

#     for i in users_list["users"]:
#         if i["name"] == user_name:
#             user_to_get = i
#         else:
#             user_to_get = 'No user found'
#     return {"username": user_to_get}


# # function definiton
# def greet(name, age):  # name, age --> parameter
#     # function body
#     return "hi" + name


# # function calling
# greet('mouse', 23)  # 'mouse' --> argument


# Query parameters

# task_name = 'learn react'
# duration = '1 month'

# Query parameters starts with ? and multiple queries are seperated by &

# http://127.0.0.1:8000/login?username=mouse&password=hello@123&location=guntur


# /tasks?task_name=learn%20react&duration=1%20month

# POST

# /tasks?status=done
# @app.get('/tasks')
# def get_tasks(status: str | None = None):
#     return {"status": status}


# Task model
# pydantic

class TaskCreate(BaseModel):
    title: str
    description: str
    completed: bool = False


tasks = []

# posting some data ----> /tasks ---> tasks = [task1, task2]
# /tasks?title=react&description=learnreact


@app.post("/tasks")
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": "Your title is " + task.title,
        "description": "The description is " + task.description,
        "completed": task.completed
    }

    tasks.append(new_task)

    return new_task

# @app.post('/login')
# @app.post('/singup')
# @app.get('/users')
# @app.get('/tasks')
# @app.get('/users/mouse')
# @app.get('/tasks/{id}')
# @app.patch('/tasks/{id}')
# @app.delete('/tasks/{id}')
