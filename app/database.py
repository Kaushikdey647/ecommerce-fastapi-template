# Import necessary modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import POSTGRES_URL

# Create an engine for PostgreSQL
engine = create_engine(
    POSTGRES_URL
)

# Create an instance of the sessionmaker class to serve as a factory for new Session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for other schemas
Base = declarative_base()

def get_db():
    """
    Dependency function to obtain a database session for use in endpoints.

    This function provides a database session to endpoints that require database access. 
    The 'yield' statement is used to generate a context manager, and the session is returned to the caller.
    The session will be automatically closed when it's no longer needed.

    Yields:
        Session: A SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        yield db  # Yield a database session
    finally:
        db.close()  # Close the session when it's no longer needed