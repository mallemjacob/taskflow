from fastapi import FastAPI

app = FastAPI()


# Get requests
@app.get('/')
def home():
    return {"message": "TaskFlow API is running"}


@app.get('/health')
def health():
    return {"status": "healthy"}


@app.get('/users')
def users():
    return {"users": [{"name": "mouse"}, {"name": "cat"}]}


@app.get('/tasks')
def tasks():
    return {"tasks": [{"task1": "learn fastapi"}, {"task2": "learn react"}, {"task3": "learn postgresql"}]}


# Path parameters
# /tasks/2

# Get /tasks/1
@app.get('/tasks/{task_id}')
def get_task(task_id: int):
    tasks_list = {
        "tasks": [
            {"task1": "learn fastapi"},
            {"task2": "learn react"},
            {"task3": "learn postgresql"}
        ]
    }
    return {"task_id": tasks_list["tasks"][task_id]}

# Get /users/mouse


@app.get('/users/{user_name}')
def get_user(user_name: str):
    users_list = {
        "users": [{"name": "mouse", "age": 23}, {"name": "cat", "age": 19}]}
    user_to_get = ''

    for i in users_list["users"]:
        if i["name"] == user_name:
            user_to_get = i
        else:
            user_to_get = 'No user found'
    return {"username": user_to_get}


# def greet(a: str):
#     return "hi " + a


# greet('mouse')
