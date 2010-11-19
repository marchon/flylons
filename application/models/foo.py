from meta import Session, Base
from sqlalchemy import *

class Foo(Base):
    __tablename__ = 'foo'
    id = Column('id', Integer, primary_key=True)    

    @classmethod
    def create(cls, id):
        f = Foo(id=id)
        Session.add(f)
        Session.commit()
        return f

    @classmethod
    def get(cls, id):
        return Session.query(Foo).filter(Foo.id==id).first()

    def __repr__(self):
        return "Foo(id=" + str(self.id) + ")"
