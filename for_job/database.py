from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, \
CheckConstraint, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BaseModel = declarative_base()

class Passenger(BaseModel):
    __tablename__ = 'passenger'

    name = Column(String(500), primary_key=True)
    email = Column(String(500), unique=True)
    balance = Column(Integer)


class Driver(BaseModel):
    __tablename__ = 'driver'

    name = Column(String(500), primary_key=True)
    email = Column(String(500), unique=True)


class Stadium(BaseModel):
    __tablename__ = 'stadium'

    name = Column(String(500), primary_key=True)
    address = Column(String(500), unique=True)
    capacity = Column(Integer)

class Travel(BaseModel):
    __tablename__ = 'travel'

    id = Column(Integer, primary_key=True)
    destination = Column(String(500), ForeignKey('stadium.name'))
    driver_name = Column(String(500), ForeignKey('driver.name'))
    passenger_name = Column(String(500), ForeignKey('passenger.name'))
    price = Column(Integer)

    __table_args__ = (
        CheckConstraint(and_(price >= 0, price <= 150)), {}
    )

engine = create_engine(
    "mysql+pymysql://root:10594@127.0.0.1/ghazan",
    encoding='latin1',
    echo=True
)

BaseModel.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

passenger1 = Passenger(
    name='Mohamad',
    email='baghali@baghali.com',
    balance= 1000
)
driver1 = Driver(
    name='ali',
    email = 'a@a.com'
)
stadium1 = Stadium(
    name='azadi',
    address='tehran',
    capacity=50
)
session.add_all([passenger1, driver1,])
session.flush()

