from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from puppiesDbSetup import Base, Shelter, Puppy
import sys
import datetime

engine = create_engine( 'sqlite:///puppyshelter.db')

# binds engine to Base class
Base.metadata.bind = engine

# connect engine to code executions
DBSession = sessionmaker(bind = engine)

# establish a session with a session object
session = DBSession()

def queryOne():
# query 1: Query all of the puppies and return the results in ascending alphabetical order
    allPuppies = session.query(Puppy.name).order_by(Puppy.name.asc()).all()
    for puppy in allPuppies:
        print puppy[0]
        
def queryTwo():
    """Query all of the puppies that are less than 6 months old organized by the youngest first
    DOES NOT WORK!  sqlalchemy error with datetime objects in the "for item in result:" call"""
    today = datetime.date.today()

    sixMonthsAgo = today - datetime.timedelta(days = 182)
    result = session.query(Puppy.name, Puppy.dateOfBirth)\
        .filter(Puppy.dateOfBirth >= sixMonthsAgo)\
        .order_by(Puppy.dateOfBirth.desc())

    # print the result with puppy name and dob
    for item in result:
        print "{name}: {dob}".format(name=item[0], dob=item[1])

def queryThree():
    """Query all puppies by ascending weight"""
    puppyWeights = session.query(Puppy.name, Puppy.weight).order_by(Puppy.weight.asc()).all()
    for puppy in puppyWeights:
        print "{name}: {weight}".format(name=puppy[0], weight=puppy[1])
        
def queryFour():
    """Query all puppies and group by shelter"""
    # puppyShelters = session.query(Puppy.name, Shelter.name).join(Puppy.shelter).order_by(Shelter.name).all()
    # for puppy in puppyShelters:
    #     print "{name}: {shelter}".format(name=puppy[0], shelter=puppy[1])
    result = session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Shelter.id).all()
    for item in result:
        print item[0].id, item[0].name, item[1]
###################
# allPuppies = session.query(Puppy.dateOfBirth).order_by(Puppy.dateOfBirth.asc()).all()
# for puppy in allPuppies:
#     print puppy[0]

queryFour()
# # display names of all entries in MenuItems tables
# items = session.query(MenuItem).all()
# for item in items:
    # print item.name()