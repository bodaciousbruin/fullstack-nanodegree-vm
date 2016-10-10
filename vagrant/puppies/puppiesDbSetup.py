import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'shelter'
    
    name = Column( String(80), nullable = False)
    address = Column( String(100))
    city = Column(String(100))
    state = Column(String(50))
    zipCode = Column(Integer)
    website = Column(String(250))
    id = Column(Integer, primary_key = True)

class Puppy(Base):
    __tablename__ = 'puppy'
    
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    dateOfBirth = Column(DateTime)
    gender = Column(String(6))
    weight = Column(String(10))
    picture = Column(String(250))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)


##################### all code above this line ################

engine = create_engine( 'sqlite:///puppies.db')
Base.metadata.create_all(engine)