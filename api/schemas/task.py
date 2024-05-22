from typing import Optional, Literal

from pydantic import BaseModel, Field

class Task(BaseModel):
    id: int
    title: str = Field(None, example="クリーニング")
    description: Optional[str] = Field(None, example="クリーニングを取りに行く")
    status: Literal["todo", "doing", "done"] = Field(None, description="現在の状態")
    
class TaskCreate(BaseModel):
    title: str = Field(None, example="クリーニング")
    description: Optional[str] = Field(None, example="クリーニングを取りに行く")
    # statusはtodoからスタート