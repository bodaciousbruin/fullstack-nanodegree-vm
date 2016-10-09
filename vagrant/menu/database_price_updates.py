veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for veggieBurger in veggieBurgers:
     print veggieBurger.id
     print veggieBurger.price
     print veggieBurger.restaurant.name
     print "\n"

# updates prices of all veggie burgers to be $2.99
for veggieBurger in veggieBurgers:
    if veggieBurger.price != '$2.99':
        veggieBurger.price = '$2.99'
        session.add(veggieBurger)
        session.commit()

for veggieBurger in veggieBurgers:
     print veggieBurger.id
     print veggieBurger.price
     print veggieBurger.restaurant.name
     print "\n"