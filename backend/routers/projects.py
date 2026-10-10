from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models import Project, Task
from schemas import ProjectCreate, ProjectResponse, ProjectUpdate, TaskResponse


router = APIRouter(
    prefix='/projects',
    tags=["Projects"]
)


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.get(Project, project_id,)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.post(
    "",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_project(data: ProjectCreate, db: Session = Depends(get_db),):
    project = Project(**data.model_dump())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


@router.get("", response_model=list[ProjectResponse], )
def get_projects(db: Session = Depends(get_db),):
    return db.scalars(
        select(Project).order_by(Project.id)
    ).all()


@router.get("/{project_id}/tasks", response_model=list[TaskResponse],)
def get_project_tasks(
    project_id: int,
    db: Session = Depends(get_db),
):
    project = db.get(
        Project,
        project_id
    )

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    return db.scalars(
        select(Task)
        .where(Task.project_id == project_id)
        .order_by(Task.id)
    ).all()


# PATCH
@router.patch("/{project_id}", response_model=ProjectResponse)
def update_project(project_id: int, changes: ProjectUpdate, db: Session = Depends(get_db),):
    project = db.get(Project, project_id)

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    update_data = changes.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(project, field, value)

    db.commit()
    db.refresh(project)
    return project


# Delete
@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.get(Project, project_id,)

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    project_tasks = db.scalars(select(Task).where(
        Task.project_id == project_id)).all()

    for task in project_tasks:
        db.delete(task)

    # Delete referencing tasks before their project, within the same transaction.
    db.flush()

    db.delete(project)
    db.commit()
