from persistence import Database
from flask import jsonify, make_response

db = Database()


def add_user(first_name, last_name, birthday, email, phone):
    user = db.add_user(first_name, last_name, birthday, email, phone)
    if user is not None:
        return make_response(jsonify(category='created',
                                     data=user.to_dict()), 201)
    return get_404()


def get_user_by_id(user_id):
    user = db.get_user_by_id(user_id)
    if user is not None:
        return make_response(jsonify(category='success',
                                     data=user.to_dict()), 200)
    return get_404()


def get_user_by_email(email):
    user = db.get_user_by_email(email)
    if user is not None:
        return make_response(jsonify(category='success',
                                     data=user.to_dict()), 200)
    return get_404()


def get_404():
    return make_response(jsonify(category='failed'), 404)
