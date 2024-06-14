from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "mysql+pymysql://root:root@localhost/shopping"

engine = create_engine(DATABASE_URL)

sessionLocal=sessionmaker(autocommit=False, bind=engine)

Base = declarative_base()

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()