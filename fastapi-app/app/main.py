from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List
from uuid import uuid4
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware to allow requests from frontend origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database configuration - Using SQLite
DATABASE_URL = "sqlite:///./dockerhub.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session factory for database sessions
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for SQLAlchemy models
Base = declarative_base()


# SQLAlchemy model for Docker repository table
class DockerRepository(Base):
    __tablename__ = "docker_repositories"

    id = Column(String, primary_key=True, index=True)
    image_name = Column(String, index=True, nullable=False)
    tag = Column(String, nullable=False)
    token = Column(String, nullable=False)


# Create tables if they don't exist
Base.metadata.create_all(bind=engine)


# Pydantic schema for incoming create request
class DockerRepoRequest(BaseModel):
    image_name: str
    tag: str
    token: str


# Pydantic schema for list/get response
class DockerRepoResponse(BaseModel):
    id: str
    image_name: str
    tag: str


# Dependency to get DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    """
    Root endpoint to check if API is running
    """
    return {"message": "FastAPI DockerHub API is working"}


@app.post("/repository", status_code=status.HTTP_201_CREATED)
def create_repository(
    req: DockerRepoRequest, db: Session = Depends(get_db)
):
    """
    Create a new Docker repository record
    Returns:
        JSON with status code, message, and new repo ID
    """
    repo_id = str(uuid4())
    new_repo = DockerRepository(
        id=repo_id,
        image_name=req.image_name,
        tag=req.tag,
        token=req.token,
    )
    db.add(new_repo)
    db.commit()
    db.refresh(new_repo)

    return {
        "status code": 201,
        "message": "Repository created successfully",
        "id": repo_id,
    }


@app.get("/repository", status_code=status.HTTP_200_OK)
def list_repositories(db: Session = Depends(get_db)):
    """
    List all Docker repositories
    Returns:
        JSON with status code, message, and list of repositories
    """
    repos = db.query(DockerRepository).all()
    repo_list = [
        {"id": r.id, "image_name": r.image_name, "tag": r.tag} for r in repos
    ]
    return {
        "status code": 200,
        "message": "Repositories fetched successfully",
        "repositories": repo_list,
    }


@app.get("/repository/{repo_id}", status_code=status.HTTP_200_OK)
def get_repository(repo_id: str, db: Session = Depends(get_db)):
    """
    Get a single Docker repository by ID
    Returns:
        JSON with status code, message, and repo details
    Raises:
        404 HTTPException if repo not found
    """
    repo = db.query(DockerRepository).filter(DockerRepository.id == repo_id).first()
    if not repo:
        raise HTTPException(status_code=404, detail="Repository not found")

    return {
        "status code": 200,
        "message": "Repository fetched successfully",
        "id": repo.id,
        "image_name": repo.image_name,
        "tag": repo.tag,
    }
