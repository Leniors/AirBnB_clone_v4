#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import *
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

# creation of a State
nairobi = State(name="Nairobi")
nairobi.save()

mombasa = State(name="Mombasa")
mombasa.save()

kisii = State(name="Kisii")
kisii.save()

# creation of a City
runda = City(state_id=nairobi.id, name="Runda")
runda.save()

lavington = City(state_id=nairobi.id, name="Lavington")
lavington.save()

karen = City(state_id=nairobi.id, name="Karen")
karen.save()

changamwe = City(state_id=mombasa.id, name="Changamwe")
changamwe.save()

nyali = City(state_id=mombasa.id, name="Nyali")
nyali.save()

nyanchwa = City(state_id=kisii.id, name="Nyanchwa")
nyanchwa.save()

mwembe = City(state_id=kisii.id, name="Mwembe")
mwembe.save()

# creation of a User
leeroy = User(email="leeroy@snow.com", password="johnpwd")
leeroy.save()

joy = User(email="joy@snow.com", password="johnpwd")
joy.save()

cathy = User(email="cathy@snow.com", password="johnpwd")
cathy.save()

master = User(email="master@snow.com", password="johnpwd")
master.save()

# creation of 2 Places
place_1 = Place(user_id=leeroy.id, city_id=runda.id, name="House 1")
place_1.save()

place_2 = Place(user_id=leeroy.id, city_id=runda.id, name="House 2")
place_2.save()

place_3 = Place(user_id=joy.id, city_id=lavington.id, name="House 3")
place_3.save()

place_4 = Place(user_id=cathy.id, city_id=karen.id, name="House 4")
place_4.save()

place_5 = Place(user_id=master.id, city_id=changamwe.id, name="Kwapedi")
place_5.save()

# creation of 3 various Amenity
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()
amenity_4 = Amenity(name="Kitchen")
amenity_4.save()
amenity_5 = Amenity(name="Chef")
amenity_5.save()
amenity_6 = Amenity(name="Studio")
amenity_6.save()

# link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)
place_1.amenities.append(amenity_4)
place_1.amenities.append(amenity_5)
place_1.amenities.append(amenity_6)

# link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

place_3.amenities.append(amenity_1)
place_3.amenities.append(amenity_2)
place_3.amenities.append(amenity_3)
place_3.amenities.append(amenity_4)

place_4.amenities.append(amenity_1)
place_4.amenities.append(amenity_2)

place_5.amenities.append(amenity_1)
place_5.amenities.append(amenity_2)
place_5.amenities.append(amenity_6)

storage.save()

print("OK")
