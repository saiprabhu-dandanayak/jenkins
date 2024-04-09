from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import DATABASE_URL


DEFAULT_DATABASE_URL = 'sqlite:///./test.db'


database_url = DATABASE_URL if DATABASE_URL else DEFAULT_DATABASE_URL

engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(bind=engine)

sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
