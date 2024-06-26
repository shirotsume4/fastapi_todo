from sqlalchemy import Column, Integer, String

from api.db import Base


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(1024))
    description = Column(String(1024), nullable=True)
    status = Column(String(1024))
