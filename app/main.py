from fastapi import FastAPI
from database import engine,Base
from routes import auth,student,admin


app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(student.router)
app.include_router(admin.router)
