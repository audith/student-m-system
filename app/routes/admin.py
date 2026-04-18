
from fastapi import APIRouter, Depends,FastAPI

from backend.app.models import Student, User
from backend.app.routes.student import get_db

router = APIRouter(prefix="/admin")
@router.get("/stats")
def stats(db=Depends(get_db)):
    students = db.query(Student).count()
    users = db.query(User).count()

    return {
        "total_students": students,
        "total_users": users
    }