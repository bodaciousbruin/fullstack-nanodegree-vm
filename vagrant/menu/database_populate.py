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

# myFirstRestaurant = Restaurant(name = "Pizza Port")
# session.add(myFirstRestaurant)
# session.commit()

# # get reference to the database object
# # session.query(Restaurant).all()

# pizzaCarlsbad = MenuItem(name = "Pizza Carlsbad", description = "Ham, pineapple, garlic, onions", course = "Entree", price = "$11.99", restaurant = myFirstRestaurant)
# session.add(pizzaCarlsbad)
# session.commit()

# get a single row from the db
dbRow = session.query(Restaurant).first()
dbRow.name #returns the value in the 'name' column of this db row

# display names of all entries in MenuItems tables
items = session.query(MenuItem).all()
for item in items:
    print item.name()