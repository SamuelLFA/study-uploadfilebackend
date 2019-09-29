import os
from flask import request, jsonify, url_for, send_from_directory
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename

from app import app
from configs.db_connection import files

class UploadFile(Resource):
  # upload file
  @jwt_required
  def post(self):

    filename = request.args.get('filename').split('/')[-1]
    filename = secure_filename(filename)
    
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, '../uploads/{}'.format(filename)), 'bw') as f:
      chunk_size = 4096
      while True:
        chunk = request.stream.read(chunk_size)
        if len(chunk) == 0:
          break
        f.write(chunk)
    
    files.insert({
      'Filename': filename,
      'User_email': get_jwt_identity(),
    })

    json = {
      'status': 200,
      'message': url_for('uploadfile', filename=filename)
    }

    return jsonify(json)

class GetFileList(Resource):
  # list file uploaded by user 
  @jwt_required
  def get(self):

    list_items = []
    items = files.find({'User_email': get_jwt_identity()})

    for item in items:
      list_items.append(item.get('Filename'))

    json = {
      'status': 200,
      'message': list_items
    }

    return jsonify(json)
