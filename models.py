from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, VARCHAR, create_engine, Computed
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(".env"))
DB_USERNAME = os.getenv("DB_USERNAME", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "post")
DB_PORT = os.getenv("DB_PORT", 5432)

engine = create_engine(
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost/prod",
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=2,
    pool_recycle=300,
    pool_use_lifo=True,
)
Base = declarative_base()
session = Session(engine)


class Recruit(Base):
    __tablename__ = "recruits"

    id = Column(Integer, primary_key=True)
    first_name = Column(VARCHAR(20), nullable=False)
    surname = Column(VARCHAR(20), nullable=False)
    rocketchat_user = Column(VARCHAR(20), nullable=False, unique=True)
    github_name = Column(VARCHAR(20), nullable=False, unique=True)
    personal_email_address = Column(VARCHAR(30), nullable=False, unique=True)
    cohort = Column(VARCHAR(20), nullable=False)

    def __repr__(self):
        return f"Recruit<Full Name:{self.first_name} {self.surname}>"
