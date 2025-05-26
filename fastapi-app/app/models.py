from sqlalchemy import Column, String, Integer
from app.database import Base

class DockerRepo(Base):
    __tablename__ = "docker_repositories"

    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String, nullable=False)
    tag = Column(String, nullable=False)
    token = Column(String, nullable=False)
