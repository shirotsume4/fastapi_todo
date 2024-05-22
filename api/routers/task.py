from typing import List
from api.schemas import task as task_schema
from api.cruds import task as task_crud
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.db import get_db

router = APIRouter()

@router.get("/tasks", response_model=List[task_schema.Task])
def get_tasks(db: AsyncSession = Depends(get_db)):
    return task_crud.get_tasks(db)


@router.post("/tasks")
def create_task(task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)):
    return task_crud.create_task(db, task_body)

@router.put("/tasks/{task_id}/todo")
def task_todo(task_id: int):
    pass

@router.put("/tasks/{task_id}/done")
def task_done(task_id: int):
    pass

@router.put("/tasks/{task_id}/doing")
def task_doing(task_id: int):
    pass

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    pass

    
