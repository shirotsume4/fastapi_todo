from typing import Optional, Literal

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str = Field(None, example="クリーニング")
    description: Optional[str] = Field(None, example="クリーニングを取りに行く")
    status: Literal["done", "todo", "doing"] = Field("todo", example="todo")

    class Config:
        from_attriubtes = True


class Task(TaskBase):
    id: int
    status: Literal["done", "todo", "doing"] = Field("todo", example="todo")

    class Config:
        from_attriubtes = True


class TaskCreate(TaskBase):
    # statusはtodoからスタート
    class Config:
        from_attriubtes = True
