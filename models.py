from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "mysql+pymysql://root:qwerty@127.0.0.1:33061/portal"
)

Base = declarative_base(bind=engine)
