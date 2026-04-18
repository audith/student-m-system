from fastapi import APIRouter, Depends
from app.database import SessionLocal
from app.models import Student, User

router = APIRouter(prefix="/admin")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/stats")
def stats(db=Depends(get_db)):
    students = db.query(Student).count()
    users = db.query(User).count()

    return {
        "total_students": students,
        "total_users": users
    }