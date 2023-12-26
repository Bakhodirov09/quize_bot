import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from data.config import DB_URL

database = databases.Database(DB_URL)

Base = declarative_base()
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DB_URL)
metadata.create_all(engine)
