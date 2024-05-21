from fastapi import APIRouter

router = APIRouter()

@router.get("/tasks")
def get_tasks():
    return [{"id": 1, "name": "task 1", "status": "todo"}]

@router.post("/tasks")
def create_task():
    pass

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

    
