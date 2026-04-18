from fastapi import APIRouter, Depends
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter(prefix="/students")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_student(student: schemas.StudentBase, db=Depends(get_db)):
    return crud.create_student(db, student)

@router.get("/")
def list_students(db=Depends(get_db)):
    return crud.get_students(db)

@router.delete("/{student_id}")
def remove_student(student_id: int, db=Depends(get_db)):
    return crud.delete_student(db, student_id)