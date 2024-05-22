from fastapi import APIRouter
from typing import List
from api.schemas import task as task_schema
from api.cruds import task as task_crud
router = APIRouter()

@router.get("/tasks", response_model=List[task_schema.Task])
def get_tasks():
    return task_crud.get_tasks()


@router.post("/tasks")
def create_task(task_body: task_schema.TaskCreate):
    return task_crud.create_task(task_body)

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

    
