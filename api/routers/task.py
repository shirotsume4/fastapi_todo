from typing import List, Literal
from sqlalchemy.orm import Session
from api.schemas import task as task_schema
from api.cruds import task as task_crud
from fastapi import APIRouter, Depends, HTTPException
from api.db import get_db

router = APIRouter()


@router.get("/tasks", response_model=List[task_schema.Task])
def get_tasks(db: Session = Depends(get_db)):
    return task_crud.get_tasks(db)


@router.get("/tasks/{task_id}", response_model=task_schema.Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return task_crud.get_task(db, task_id)


@router.post("/tasks")
def create_task(task_body: task_schema.TaskCreate, db: Session = Depends(get_db)):
    try:
        task_crud.create_task(db, task_body)
        return "post ok"
    except HTTPException as e:
        raise e


@router.put("/tasks/{task_id}")
def task_todo(
    task_id: int,
    status: Literal["done", "todo", "doing"],
    db: Session = Depends(get_db),
):
    try:
        task_crud.update_task_status(db, task_id, status)
        return "put ok"
    except HTTPException as e:
        raise e


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    try:
        task_crud.delete_task(db, task_id)
        return "delete ok"
    except HTTPException as e:
        raise e
