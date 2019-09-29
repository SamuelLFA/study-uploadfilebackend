from flask import request, jsonify
from flask_restful import Api, Resource

from app import app
from configs.jwt import JWT

from controllers.UserController import Register, Login
from controllers.FileController import UploadFile, GetFileList

api = Api(app)
JWT().configure_jwt(app)

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(UploadFile, '/upload')
api.add_resource(GetFileList, '/getFileList')