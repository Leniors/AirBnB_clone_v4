#!/usr/bin/python3
"""
handle State objects
"""
from flask import jsonify, abort, request
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from api.v1.views import app_views


@app_views.route('/places', methods=['GET'], strict_slashes=False)
def get_places():
    places = storage.all(Place)
    if not places:
        abort(404)
    return jsonify([place.to_dict() for place in places.values()]), 200


@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_places_with_city_id(city_id):
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    temp = city.__dict__['_sa_instance_state']
    st = temp.obj
    city_object = st()
    places_in_city = city_object.places
    return jsonify([place.to_dict() for place in places_in_city]), 200


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict()), 200


@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def create_place(city_id):
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    if 'user_id' not in request.json:
        abort(400, description="Missing user_id")
    data = request.json
    data.update({"city_id": city_id})
    new_place = Place(**data)
    new_place.save()
    return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.json
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(place, key, value)
    place.save()
    return jsonify(place.to_dict()), 200
