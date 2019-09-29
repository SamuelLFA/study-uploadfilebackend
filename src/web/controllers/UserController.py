from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_refresh_token_required, get_jwt_identity
import bcrypt

from helpers.user_helper import userExist, verifyUser
from configs.db_connection import users

# register user
class Register(Resource):
  def post(self):
    data = request.get_json()

    email = data['email']
    password = data['password']

    if userExist(email):
      json = {
        'status': 401,
        'message': 'Invalid email'
      }
      return jsonify(json)

    password_hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    users.insert({
      'Email': email,
      'Password': password_hash,
    })

    token = create_access_token(email)

    json = {
      'status': 200,
      'message': token
    }

    return jsonify(json)

# login user
class Login(Resource): 
  def post(self):
    data = request.get_json()

    email = data['email']
    password = data['password']

    if not userExist(email):
      json = {
        'status': 401,
        'message': 'Invalid Email'
      }
      return jsonify(json)

    correct_password = verifyUser(email, password)

    if not correct_password:
      json= {
        'status': 401,
        'message': 'Invalid password'
      }
      return jsonify(json)

    token = create_access_token(email)

    json = {
      'status': 200,
      'message': token
    }
    return jsonify(json)