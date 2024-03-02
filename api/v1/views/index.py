#!/usr/bin/python3
"""
index file
"""
from api.v1.views import app_views
from flask import jsonify
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


@app_views.route('/status', strict_slashes=False)
def get_status():
    """status of the request"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def get_stats():
    """stats"""
    classes = {"Amenity": Amenity,
               "City": City,
               "Place": Place,
               "Review": Review,
               "State": State,
               "User": User}
    stats = {}
    for cls in classes.keys():
        if cls == "Amenity":
            stats["amenities"] = storage.count(classes[cls])
        elif cls == "City":
            stats["cities"] = storage.count(classes[cls])
        elif cls == "Place":
            stats["places"] = storage.count(classes[cls])
        elif cls == "Review":
            stats["reviews"] = storage.count(classes[cls])
        elif cls == "State":
            stats["states"] = storage.count(classes[cls])
        elif cls == "User":
            stats["uers"] = storage.count(classes[cls])
    return jsonify(stats)
