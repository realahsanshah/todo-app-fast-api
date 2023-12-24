import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Create the database URL
db_url = os.getenv("SQLALCHEMY_DATABASE_URL")

# Create the engine
engine = create_engine(db_url)


# Test the connection
try:
    with engine.connect():
        print("Connected to the PostgreSQL database!")
except Exception as e:
    print("Failed to connect to the PostgreSQL database:", str(e))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# get database 
def get_db():
    db = engine.connect()
    try:
        yield db
    finally:
        db.close()