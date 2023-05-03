from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://renzomatias:rm02cm02@db4free.net:3306/djangotest"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind = engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
        db.refresh(db)
    except:
        db.rollback()
    finally:
        db.close()
