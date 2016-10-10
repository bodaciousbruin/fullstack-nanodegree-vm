from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppiesDbSetup import Base, Shelter, Puppy
import sys
import datetime

engine = create_engine( 'sqlite:///puppies.db')

# binds engine to Base class
Base.metadata.bind = engine

# connect engine to code executions
DBSession = sessionmaker(bind = engine)

# establish a session with a session object
session = DBSession()

# get a single row from the db
allPuppies = session.query(Puppy).all()
for puppy in allPuppies:
    print puppy.name()

# # display names of all entries in MenuItems tables
# items = session.query(MenuItem).all()
# for item in items:
    # print item.name()