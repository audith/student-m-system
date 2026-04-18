from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base, SessionLocal
from app.routes import auth, student, admin
from app.models import User
from app.auth import hash_password

app = FastAPI(
    title="Student Management System",
    version="1.0.0"
)

# 🔥 CORS (IMPORTANT for React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # in production: use your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🗄️ Create tables
Base.metadata.create_all(bind=engine)


# 👑 Auto-create Admin on startup
@app.on_event("startup")
def create_admin():
    db = SessionLocal()

    admin = db.query(User).filter(User.email == "admin@gmail.com").first()

    if not admin:
        new_admin = User(
            email="admin@gmail.com",
            hashed_password=hash_password("admin123"),
            role="admin"
        )
        db.add(new_admin)
        db.commit()
        print("✅ Admin created: admin@gmail.com / admin123")

    db.close()


# 🔗 Routers
app.include_router(auth.router, tags=["Auth"])
app.include_router(student.router, tags=["Students"])
app.include_router(admin.router, tags=["Admin"])


# ❤️ Health check (very useful)
@app.get("/")
def root():
    return {"message": "API is running 🚀"}