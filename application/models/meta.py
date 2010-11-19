from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Session = scoped_session(sessionmaker())
Base = declarative_base()
