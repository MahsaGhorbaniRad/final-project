from sqlalchemy import Boolean, Column, Integer, String , Float
from database import Base


class course(Base):

    __tablename__ = "course"

    cid = Column(String , primary_key=True)
    cname = Column(String)
    department = Column(String)
    credit = Column(Integer)


class student(Base):

    __tablename__ = "student"

    sid = Column(String , primary_key=True)
    Fname = Column(String)
    Lname = Column(String)
    Father_name = Column(String)
    Birth_date = Column(String)
    IDS = Column(String)
    Born_city = Column(String)
    Address = Column(String)
    Postal_code = Column(Integer)
    Cphone = Column(Integer)
    Hphone = Column(Integer)
    department = Column(String)
    major = Column(String)
    Married = Column(Boolean)
    ID = Column(String)


class lecturer(Base):

    __tablename__ = "lecturer"

    Lid = Column(String , primary_key=True)
    Fname = Column(String)
    Lname= Column(String)
    ID = Column(String)
    department = Column(String)
    major = Column(String)
    birth_date = Column(String)
    born_city = Column(String)
    Address = Column(String)
    postal_code = Column(Integer)
    Cphone = Column(Integer)
    Hphone = Column(Integer)
