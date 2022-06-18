from flask import Blueprint, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

biblioteca_routes = Blueprint('biblioteca_routes', __name__)

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@biblioteca_routes.route('/biblioteca/insert')
def test():
    try:
        db.collection('traduccion').add({
            'email': 'nuevocorreo@gmail.com',
            'idm_origen': 'eng',
            'idm_traduc': 'esp',
            'txt_origen': 'Test',
            'txt_traduc': 'Prueba',
            'imagen': 'http://'
        })
    except Exception as e:
        print(f'Exception: {e}')

    return jsonify({'msg': 'Insertado en Biblioteca'})

@biblioteca_routes.route('/biblioteca/listar')
def list():
    return [doc.to_dict() for doc in db.collection('traduccion').stream()]