from datetime import datetime
from flask_cors import cross_origin
from flask import Blueprint, jsonify, request

from src.utils.db import connect_database

task = Blueprint('task', __name__)

db = connect_database()


@task.route('/', methods=['POST'])
def insert():
    try:
        data = request.json
        nuevo = {
            'user': data['user'],
            'description': data['description'],
            'date': data['date'],
            'date_created': datetime.today()
        }
        db.collection('task').add(nuevo)
        return jsonify({
            'msg': 'Insertado correctamente',
            'insert': nuevo
        }), 200
    except Exception as e:
        return jsonify({
            'error': f'Exception: {e}'
        }), 400


@task.route('/', methods=['GET'])
def getBilbliotecaEmail():
    datos=[doc.to_dict() for doc in db.collection('task').stream()]
    return jsonify(datos), 200
