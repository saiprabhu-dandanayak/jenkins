
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import DATABASE_URL


database_url=DATABASE_URL

engine=create_engine(database_url)

Base=declarative_base()


sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
