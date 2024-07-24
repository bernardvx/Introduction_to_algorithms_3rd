from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
import os

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")



def create_conn():
    engine = None
    while not engine:
        try:
            engine = create_engine(
                SQLALCHEMY_DATABASE_URL
            )
        except:
            print("could not connect to database\ntrying again...")
            time.sleep(5)
    print("connected to database")
    return engine

engine = create_conn()



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

