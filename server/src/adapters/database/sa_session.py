from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.adapters.database.settings import settings

engine = create_engine(settings.SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
