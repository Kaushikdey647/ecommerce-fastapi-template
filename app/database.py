# import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# create engine for postgresql

POSTGRES_URL = "postgresql://postgres:postgres@localhost:5432/backend_db" 

engine = create_engine(
    POSTGRES_URL
)

# an instance of the sessionmaker class, which will serve as a factory for new Session objects
# incase you're 5, its a database session, you can use it
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# we use this as a base class for other schemas
Base = declarative_base()

# Dependency for all endpoints to use
def get_db():
    db = SessionLocal()
    try:
        yield db # yield is like return, but it returns a generator
    finally:
        db.close()