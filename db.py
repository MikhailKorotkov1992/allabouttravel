from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_NAME = 'allabouttravel.sqlite3'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
<<<<<<< HEAD
Base.query = db_session.query_property
=======
Base.query = db_session.query_property
>>>>>>> 5b890b971f0c88fb59b6c78d3f35a4a480d86f1c
