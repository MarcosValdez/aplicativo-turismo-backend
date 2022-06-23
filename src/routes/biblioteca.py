import firebase_admin
from firebase_admin import credentials, firestore

from flask import Blueprint, jsonify, render_template, request

from src.utils import connect_database

biblioteca_routes = Blueprint('biblioteca_routes', __name__)

db = connect_database()

@biblioteca_routes.route('/biblioteca/insert', methods=['POST'])
def insert():
    try:
        data = request.json
        nuevo = {
            'email': data['email'],
            'idm_origen': data['idm_origen'],
            'idm_traduc': data['idm_traduc'],
            'txt_origen': data['txt_origen'],
            'txt_traduc': data['txt_traduc'],
            'imagen': data['img'],
        }
        db.collection('traduccion').add(nuevo)
        return jsonify({
            'msg': 'Insertado en Biblioteca',
            'insert': nuevo
        }), 200
    except Exception as e:
        return jsonify({
            'error': f'Exception: {e}'
        }), 400

@biblioteca_routes.route('/biblioteca/listarEmail', methods=['POST'])
def getBilbliotecaEmail():
    lista = []
    data = request.json
    datos = db.collection('traduccion').where('email', "==", data['email']).stream()
    for doc in datos:
        nuevo = doc.to_dict()
        nuevo['doc_id'] = doc.id
        lista.append(nuevo)
    if len(lista) == 0:
        return jsonify({
            "error": "El usuario no tiene traducciones"
        }), 404
    else:
        return jsonify(lista), 200


@biblioteca_routes.route('/listar')
def list():
    lista = []
    datos = db.collection('traduccion').stream()
    for doc in datos:
        nuevo = doc.to_dict()
        nuevo['doc_id'] = doc.id
        lista.append(nuevo)
    return jsonify(lista), 200

@biblioteca_routes.route('/biblioteca/delete', methods=['DELETE'])
def delete():
    try:
        data = request.json
        document = db.collection('traduccion').document(data['id'])
        doc = document.get()
        if doc.exists:
            document.delete()
            return jsonify({
                'msg': 'Traduccion eliminada',
                'doc': doc.to_dict()
            }), 200
        else:
            return jsonify({
                'error': 'El documento no existe'
            }), 400

    except Exception as e:
        return jsonify({
            'error': f'Exception: {e}'
        }), 400

@biblioteca_routes.route('/biblioteca/update', methods=['POST'])
def update():
    try:
        data = request.json
        document = db.collection('traduccion').document(data['doc_id'])
        doc = document.get()
        if doc.exists:
            document.update({
                'idm_origen': data['idm_origen'],
                'idm_traduc': data['idm_traduc'],
                'txt_origen': data['txt_origen'],
                'txt_traduc': data['txt_traduc'],
                'imagen': data['img'],
            })
            doc = document.get()
            return jsonify({
                'msg': 'Traduccion actualizada',
                'doc': doc.to_dict()
            }), 200
        else:
            return jsonify({
                'error': 'El documento no existe'
            }), 400

    except Exception as e:
        return jsonify({
            'error': f'Exception: {e}'
        }), 400

@biblioteca_routes.route("/biblioteca/dashboard")
def dashboard():
    datos = [doc.to_dict() for doc in db.collection('traduccion').stream()]
    return render_template('dashboard.html', datos=datos)

