from fastapi import FastAPI
from routers import user
from db.session import Base , engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

Base.metadata.create_all(bind=engine)

app.include_router(user.router)

