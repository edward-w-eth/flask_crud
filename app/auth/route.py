from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from flask.views import MethodView

from app import db
from app.auth.models import User

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/register', methods=['POST'])
def register():
        post_data = request.json

        user = User.query.filter_by(email=post_data['email']).first()

        if not user:
            try:
                user = User(
                    email=post_data['email'],
                    password=post_data['password']
                )
                # insert the user
                user.save()
                # generate the auth token
                auth_token = create_access_token(identity={'email': user.email, 'user_id': user.id})
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                    'auth_token': auth_token
                }
                return jsonify(responseObject), 201
            except Exception as e:
                print(e)
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occurred. Please try again.'
                }
                return jsonify(responseObject), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return jsonify(responseObject), 202

@auth_blueprint.route('/login', methods=['POST'])
def login():
    # get the post data
    post_data = request.json
    try:
        # fetch the user data
        user = User.query.filter_by(
            email=post_data.get('email')
        ).first()
        if user and user.password_is_valid(post_data.get('password')):
            auth_token = create_access_token(identity={'email': user.email, 'user_id': user.id})
            if auth_token:
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'auth_token': auth_token
                }
                return jsonify(responseObject), 200
        else:
            responseObject = {
                'status': 'fail',
                'message': 'User does not exist.'
            }
            return jsonify(responseObject), 404
    except Exception as e:
        print(e)
        responseObject = {
            'status': 'fail',
            'message': 'Try again'
        }
        return jsonify(responseObject), 500
