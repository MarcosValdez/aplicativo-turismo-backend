from datetime import datetime
from pydoc import doc
import uuid
from flask_cors import cross_origin
from flask import Blueprint, jsonify, request

from src.utils.db import connect_database

task = Blueprint('task', __name__)

db = connect_database()


@task.route('/', methods=['GET'])
def getTasks():
    datos = [doc.to_dict() for doc in db.collection('task').stream()]
    return jsonify(datos), 200


@task.route('/<string:task_id>', methods=['GET'])
def getTaskbyId(task_id):
    document = db.collection('task').document(task_id)
    return jsonify(document.get().to_dict()), 200


@task.route('/user/<string:user>', methods=['GET'])
def getTaskByUser(user):
    datos = [doc.to_dict() for doc in db.collection(
        'task').where('user_id', '==', user).stream()]
    return jsonify(datos), 200


@cross_origin
@task.route('/', methods=['POST'])
def insert():
    try:
        data = request.json
        nuevo = {
            'task_id': uuid.uuid4().hex,
            'user_id': data['user'],
            'description': data['description'],
            'date': data['date'],
            'date_created': datetime.today(),
            'date_update': '',
            'active': True
        }
        # db.collection('task').add(nuevo)
        db.collection('task').document(nuevo['task_id']).set(nuevo)
        return jsonify({
            'msg': 'Insertado correctamente',
            'insert': nuevo
        }), 200
    except Exception as e:
        return jsonify({
            'error': f'Exception: {e}'
        }), 400


@task.route('/', methods=['PUT'])
def update():
    try:
        data = request.json
        document = db.collection('task').document(data['task_id'])
        doc = document.get()
        if doc.exists:
            document.update({
                'description': data['description'],
                'date': data['date'],
                'date_update': datetime.today(),
            })
            doc = document.get()
            return jsonify({
                'msg': 'Actualizado correctamente',
                'insert': doc.to_dict()
            }), 200
        else:
            return jsonify({
                'error': 'El documento no existe'
            }), 400
    except Exception as e:
        return jsonify({
            'error': f'Exception: {e}'
        }), 400


@task.route('/<string:task_id>', methods=['DELETE'])
def delete(task_id):
    docs = db.collection('task').where('task_id', '==', task_id).stream()
    eliminados = 0
    for doc in docs:
        doc.reference.delete()
        eliminados += 1
    return jsonify(eliminados), 200
