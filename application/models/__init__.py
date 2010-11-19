from meta import Session
from sqlalchemy import create_engine

# Or you can do db_uri as a dict and configure multiple Sessions
def init_model(db_uri):
    engine = create_engine(db_uri)
    Session.configure(bind=engine)
