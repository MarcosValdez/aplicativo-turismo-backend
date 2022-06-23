from flask import Blueprint, jsonify, render_template

from src.utils import connect_database

biblioteca_routes = Blueprint('biblioteca_routes', __name__)

db = connect_database()

@biblioteca_routes.route('/insert')
def test():
    try:
        nuevo = {
            'email': 'nuevocorreo@gmail.com',
            'idm_origen': 'eng',
            'idm_traduc': 'esp',
            'txt_origen': 'Test',
            'txt_traduc': 'Prueba',
            'imagen': 'http://'
        }
        db.collection('traduccion').add(nuevo)
    except Exception as e:
        print(f'Exception: {e}')

    return jsonify({
        'msg': 'Insertado en Biblioteca',
        'note': nuevo
    })

@biblioteca_routes.route('/listar')
def list():
    lista = []
    datos = db.collection('traduccion').stream()
    for doc in datos:
        nuevo = doc.to_dict()
        lista.append(nuevo)
    return jsonify(lista)
