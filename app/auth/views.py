from flask import Blueprint, request, make_response, jsonify
from flask_jwt_extended import create_access_token
from flask.views import MethodView

from app import db
from app.auth.models import User

auth_blueprint = Blueprint('auth', __name__)

class RegisterUser(MethodView):
    """Class to Register a new user"""
    
    def post(self):
        post_data = request.get_json()

        user = User.query.filter_by(email=post_data.get('email')).first()

        if not user:
            try:
                user = User(
                    email=post_data.get('email'),
                    password=post_data.get('password')
                )
                # insert the user
                user.save()
                # generate the auth token
                auth_token = create_access_token(identity=user.email)
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                    'auth_token': auth_token
                }
                return make_response(jsonify(responseObject)), 201
            except Exception as e:
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occurred. Please try again.'
                }
                return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return make_response(jsonify(responseObject)), 202

class LoginUser(MethodView):
    """Class to login user"""
    def post(self):
        # get the post data
        post_data = request.get_json()
        try:
            # fetch the user data
            user = User.query.filter_by(
                email=post_data.get('email')
            ).first()
            if user and user.password_is_valid(post_data.get('password')):
                auth_token = create_access_token(identity=user.email)
                if auth_token:
                    responseObject = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token.decode()
                    }
                    return make_response(jsonify(responseObject)), 200
            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'User does not exist.'
                }
                return make_response(jsonify(responseObject)), 404
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(responseObject)), 500

registration_view = RegisterUser.as_view('register_api')
login_view = LoginUser.as_view('login_api')

auth_blueprint.add_url_rule(
    '/register',
    view_func=registration_view,
    methods=['POST']
)

auth_blueprint.add_url_rule(
    '/login',
    view_func=login_view,
    methods=['POST']
)