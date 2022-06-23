from flask import Blueprint, jsonify, render_template
import firebase_admin
from firebase_admin import credentials, firestore

biblioteca_routes = Blueprint('biblioteca_routes', __name__)

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@biblioteca_routes.route('/biblioteca/insert')
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

@biblioteca_routes.route('/biblioteca/listar')
def list():
    lista = []
    datos = db.collection('traduccion').stream()
    for doc in datos:
        nuevo = doc.to_dict()
        lista.append(nuevo)
    return jsonify(lista)

@biblioteca_routes.route("/dashboard")
def dashboard():
    datos = [doc.to_dict() for doc in db.collection('traduccion').stream()]
    return render_template('dashboard.html', datos=datos)