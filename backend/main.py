from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Get requests
# @app.get('/')
# def home():
#     return {"message": "TaskFlow API is running"}


# @app.get('/health')
# def health():
#     return {"status": "healthy"}


# Get All tasks
@app.get('/tasks')
def tasks():
    return tasks


# Get one task
# /tasks/1
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return {"message": "Task not found"}


# Task model
# pydantic
class TaskCreate(BaseModel):
    title: str
    description: str
    completed: bool = False


tasks = []


# Create a new task
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


# PATCH
class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None


# /tasks/6
@app.patch("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            if updated_task.title is not None:
                task["title"] = updated_task.title

            if updated_task.description is not None:
                task["description"] = updated_task.description

            if updated_task.completed is not None:
                task['completed'] = updated_task.completed

            return task

    return {"message": "Task not found"}


# Delete a task
# /tasks/3
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}

    return {"message": "Task not found"}
