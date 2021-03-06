# pip install sqlalchemy
# https://www.sqlalchemy.org/

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(100))
    password = Column(String(50))

    def __repr__(self):
        return "<User(name=%s, fullname=%s, password=%s)>" % \
               (self.name, self.fullname, self.password)
