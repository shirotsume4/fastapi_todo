import api.models.task as task_model
import api.schemas.task as task_schema

def create_task(db, task_body):
    task = task_model.Task(title=task_body.title, description=task_body.description, status="todo")
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks(db):
    return db.query(task_model.Task).all()