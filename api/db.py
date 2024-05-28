from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "mysql+pymysql://root@db:3306/demo"
engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    try:
        db = SessionLocal()  # sessionを生成
        yield db
    finally:
        db.close()
