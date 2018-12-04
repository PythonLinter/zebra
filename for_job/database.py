from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, \
CheckConstraint, and_, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

BaseModel = declarative_base()



travel_passenger = Table(
    'travel_passenger',
    BaseModel.metadata,
    Column(
        'passenger_id',
        String(500),
        ForeignKey('passenger.name'),
        primary_key=True,
    ),
    Column(
        'tarvel_id',
        Integer,
        ForeignKey('travel.id'),
        primary_key=True
    )
)


travel_driver = Table(
    'travel_driver',
    BaseModel.metadata,
    Column(
        'driver_id',
        String(500),
        ForeignKey('driver.name'),
        primary_key=True,
    ),
    Column(
        'tarvel_id',
        Integer,
        ForeignKey('travel.id'),
        primary_key=True
    )
)


travel_stadium = Table(
    'travel_stadium',
    BaseModel.metadata,
    Column(
        'stadium_id',
        String(500),
        ForeignKey('stadium.name'),
        primary_key=True,
    ),
    Column(
        'tarvel_id',
        Integer,
        ForeignKey('travel.id'),
        primary_key=True
    )
)


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
    passenger = relationship('Passenger', secondary='travel_passenger')
    driver = relationship('Driver', secondary='travel_driver')
    stadium = relationship('Stadium', secondary='travel_stadium')

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
    email='a@a.com',
)
stadium1 = Stadium(
    name='azadi',
    address='tehran',
    capacity=120
)
stadium2 = Stadium(
    name='shirudi',
    address='shiraz',
    capacity=150
)
travel1 = Travel(
    stadium=[stadium1],
    driver=[driver1],
    passenger=[passenger1]
)
session.add_all([passenger1, driver1,travel1,stadium1, stadium2])
session.flush()
stadiums = session.query(Stadium).all()

for element in stadiums:
    element.capacity = element.capacity-50
session.commit()
