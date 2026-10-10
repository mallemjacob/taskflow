from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models import Project, Task
from schemas import TaskCreate, TaskResponse, TaskUpdate


router = APIRouter(
    prefix='/tasks',
    tags=["Tasks"]
)


@router.get("", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.scalars(select(Task).order_by(Task.id)).all()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# Create a new task
@router.post("",  response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(data: TaskCreate, db: Session = Depends(get_db)):
    project = db.get(Project, data.project_id,)

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found",)

    task = Task(**data.model_dump())

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


# PATCH
@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, changes: TaskUpdate, db: Session = Depends(get_db),):
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    for field, value in changes.model_dump(exclude_unset=True).items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task

# Delete a task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id,)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
