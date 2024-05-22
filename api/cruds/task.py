from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model
import api.schemas.task as task_schema


def create_task(
    db: AsyncSession, task_create: task_schema.TaskCreate):
    task = task_model.Task(**task_create.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks(db: AsyncSession):
    return db.query(task_model.Task).all()