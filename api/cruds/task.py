import api.models.task as task_model
import api.schemas.task as task_schema
from fastapi import HTTPException
def create_task(db, task_body: task_schema.TaskCreate):
    task = task_model.Task(
        title=task_body.title,
        description=task_body.description,
        status=task_body.status
    )
    if db.query(task_model.Task).filter(task_model.Task.title == task.title).first():
        raise HTTPException(status_code=400, detail="Task already exists")
    else:
        db.add(task)
        db.commit()
        return task

def get_tasks(db):
    return db.query(task_model.Task).all()

def get_task(db, task_id: int):
    return db.query(task_model.Task).filter(task_model.Task.id == task_id).first()

def update_task_status(db, task_id: int, status: str):
    raise HTTPException(status_code=501, detail="Not implemented")

def delete_task(db, task_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")