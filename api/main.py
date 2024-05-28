from fastapi import FastAPI
from api.routers import task
# Engine の作成
from api.db import engine
import api.db
# table作成
api.db.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(task.router)


@app.get("/")
def hello():
    return {"message": "hello world!"}
