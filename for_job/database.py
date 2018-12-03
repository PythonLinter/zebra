from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, \
CheckConstraint, and_
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class Passenger(BaseModel):
    __tablename__ = 'passanger'

    name = Column(String, primary_key=True)
    email = Column(String, unique=True)
    balance = Column(Integer)


class Driver(BaseModel):
    __tablename__ = 'driver'

    name = Column(String, primary_key=True)
    email = Column(String, unique=True)


class Stadium(BaseModel):
    __tablename__ = 'stadium'

    name = Column(String, primary_key=True)
    adress = Column(String, unique=True)
    capacity = Column(Integer)

class Travel(BaseModel):
    __tablename__ = 'travel'

    id = Column(Integer, primary_key=True)
    destination = Column(String, ForeignKey('stadium.name'))
    driver_name = Column(String, ForeignKey('driver.name'))
    passenger_name = Column(String, ForeignKey('passenger.name'))
    price = Column(Integer)

    __table_args__ = (
        CheckConstraint(and_(price >= 0, price <= 150)), {}
    )

engine = create_engine('mysql+pymysql://root:10594@localhost/ghazan')

