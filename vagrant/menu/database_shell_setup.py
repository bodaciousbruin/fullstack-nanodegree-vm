from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

# binds engine to Base class
Base.metadata.bind = engine

# connect engine to code executions
DBSession = sessionmaker(bind = engine)

# establish a session with a session object
session = DBSession()