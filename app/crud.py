from app.models import User, Student
from app.auth import hash_password

def create_user(db, email: str, password: str):
    user = User(email=email, hashed_password=hash_password(password))  # 🔥 fix field name
    db.add(user)
    db.commit()
    return user

def create_student(db, data):
    student = Student(**data.dict())
    db.add(student)
    db.commit()
    return student

def get_students(db):
    return db.query(Student).all()

def delete_student(db, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if student:   # ✅ avoid crash
        db.delete(student)
        db.commit()
    
    return {"message": "Student deleted"}