from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask import jsonify

from configs.db_connection import users
from controllers.UserController import Login

class JWT:
    def configure_jwt(self, app):
        jwt = JWTManager(app)
        self.parameters(app)

        @jwt.user_claims_loader
        def add_claims_to_access_token(email):
            users.find_one_and_update({"Email": email},
                                      {"$set": {"active": True}})
            return 'Authorized'

        @jwt.expired_token_loader
        def my_expired_token_callback():
            resp = jsonify({
                'status': 401,
                'sub_status': 42,
                'message': "Token expired"
            })
            resp.status_code = 401
            return resp

        @jwt.unauthorized_loader
        def my_unauthorized_callback(e):
            resp = jsonify({
                'status': 401,
                'sub_status': 1,
                'description': e,
                'message': "Credentials invalid"
            })
            resp.status_code = 401
            return resp

        @jwt.claims_verification_loader
        def my_claims_verification_callback(e):
            resp = jsonify({
                'status': 401,
                'sub_status': 2,
                'description': e,
                'message': "Credentials invalid"
            })

            resp.status_code = 401

            return resp

        @jwt.invalid_token_loader
        def my_invalid_token_loader_callback(e):
            resp = jsonify({
                'status': 401,
                'sub_status': 3,
                'description': e,
                'message': "Token invalid"
            })
            resp.status_code = 401
            return resp

        @jwt.needs_fresh_token_loader
        def my_needs_fresh_token_callback(e):
            resp = jsonify({
                'status': 401,
                'sub_status': 4,
                'description': e,
                'message': "Token invalid"
            })
            resp.status_code = 401
            return resp

        @jwt.revoked_token_loader
        def my_revoked_token_callback(e):
            resp = jsonify({
                'status': 401,
                'sub_status': 5,
                'description': e,
                'message': "Token invalid"
            })
            resp.status_code = 401
            return resp

        @jwt.user_loader_callback_loader
        def my_user_loader_callback(e):
            resp = jsonify({
                'status': 401,
                'sub_status': 6,
                'description': e,
                'message': "Token invalid"
            })
            resp.status_code = 401
            return resp

        @jwt.user_loader_error_loader
        def my_user_loader_error_callback(e):
            resp = jsonify({
                'status': 401,
                'sub_status': 7,
                'description': e,
                'message': "Token invalid"
            })
            resp.status_code = 401
            return resp

        @jwt.token_in_blacklist_loader
        def my_token_in_blacklist_callback(e):
            resp = jsonify({
                'status': 401,
                'sub_status': 8,
                'description': e,
                'message': "Token invalid"
            })
            resp.status_code = 401
            return resp

        @jwt.claims_verification_failed_loader
        def my_claims_verification_failed_callback(e):
            resp = jsonify({
                'status': 401,
                'sub_status': 9,
                'description': e,
                'message': "Token invalid"
            })
            resp.status_code = 401
            return resp
    
    def parameters(self, app):
        app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=6)
        app.config['JWT_ALGORITHM'] = 'HS512'
        app.config['JWT_SECRET_KEY'] = 'd739c8b1fe016586d23ecb7e12cae7ab'