#!/usr/bin/python3
"""
handle State objects
"""
from flask import jsonify, abort, request
from models import storage
from models.review import Review
from models.place import Place
from api.v1.views import app_views


@app_views.route('/reviews', methods=['GET'], strict_slashes=False)
def get_reviews():
    reviews = storage.all(Review)
    if not reviews:
        abort(404)
    return jsonify([review.to_dict() for review in reviews.values()]), 200


@app_views.route('/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def get_reviews_with_place_id(place_id):
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    temp = place.__dict__['_sa_instance_state']
    st = temp.obj
    place_object = st()
    review_places = place_object.reviews
    return jsonify([review.to_dict() for review in review_places]), 200


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict()), 200


@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def create_review(review_id):
    place = storage.get(Place, place_id)
    if Place is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    if 'user_id' not in request.json:
        abort(400, description="Missing user_id")
    user = storage.get(User, request.json.get(user_id))
    if user is None:
        abort(404)
    if 'text' not in request.json:
        abort(400, description="Missing text")
    data = request.json
    data.update({"place_id": place_id})
    new_review = Review(**data)
    new_review.save()
    return jsonify(new_review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.json
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict()), 200
