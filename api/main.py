from fastapi import FastAPI
from api.routers import task
app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "hello world!"}

app.include_router(task.router)