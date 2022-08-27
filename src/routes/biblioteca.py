from flask_cors import cross_origin
from flask import Blueprint, jsonify, request

from src.utils.db import connect_database

biblioteca_routes = Blueprint('biblioteca_routes', __name__)

db = connect_database()


@biblioteca_routes.route('insert', methods=['POST'])
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


@biblioteca_routes.route('listarEmail', methods=['POST'])
def getBilbliotecaEmail():
    lista = []
    data = request.json
    datos = db.collection('traduccion').where(
        'email', "==", data['email']).stream()
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


@cross_origin
@biblioteca_routes.route('/listar-continentes')
def listContinente():
    continentes = []
    datos = db.collection('continente').stream()
    for doc in datos:
        nuevo = doc.to_dict()
        nuevo['doc_id'] = doc.id
        continentes.append(nuevo)
    return jsonify(continentes), 200


@cross_origin
@biblioteca_routes.route('/listar-paises/<string:continente>')
def listPaises(continente):
    paises = []
    ##datos = db.collection('continente').stream()
    datos = db.collection('pais')
    datos_paises = datos.where('codigo', '==', continente).stream()
    for doc in datos_paises:
        nuevo = doc.to_dict()
        nuevo['doc_id'] = doc.id
        paises.append(nuevo)
    return jsonify(paises), 200

@cross_origin
@biblioteca_routes.route('/listar-cultura/<string:pais>')
def listCultura(pais):
    paises = []
    ##datos = db.collection('continente').stream()
    datos = db.collection('cultura')
    datos_paises = datos.where('pais', '==', pais).stream()
    for doc in datos_paises:
        nuevo = doc.to_dict()
        nuevo['doc_id'] = doc.id
        paises.append(nuevo)
    return jsonify(paises), 200


@cross_origin
@biblioteca_routes.route('/listar-todos-paises')
def listTodosPaises():
    paises = []
    datos = db.collection('pais').stream()
    for doc in datos:
        nuevo = doc.to_dict()
        nuevo['doc_id'] = doc.id
        paises.append(nuevo)
    return jsonify(paises), 200


@biblioteca_routes.route('/listar')
def list():
    lista = []
    datos = db.collection('traduccion').stream()
    for doc in datos:
        nuevo = doc.to_dict()
        nuevo['doc_id'] = doc.id
        lista.append(nuevo)
    return jsonify(lista), 200


@biblioteca_routes.route('/delete', methods=['DELETE'])
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


@biblioteca_routes.route('/update', methods=['POST'])
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
