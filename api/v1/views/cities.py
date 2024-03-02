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


@app_views.route('/cities', methods=['GET'], strict_slashes=False)
def get_cities():
    cities = storage.all(City)
    if not cities:
        abort(404)
    return jsonify([city.to_dict() for city in cities.values()]), 200


@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_cities_with_state_id(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    temp = state.__dict__['_sa_instance_state']
    st = temp.obj
    state_object = st()
    city_states = state_object.cities
    return jsonify([city.to_dict() for city in city_states]), 200


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict()), 200


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    city = storage.get(City, city_id)
    if state is None:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def create_city(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    if 'name' not in request.json:
        abort(400, description="Missing name")
    data = request.json
    data.update({"state_id": state_id})
    new_city = City(**data)
    new_city.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.json
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(city, key, value)
    city.save()
    return jsonify(city.to_dict()), 200
