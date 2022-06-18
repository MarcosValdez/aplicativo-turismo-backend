from flask import Blueprint
import firebase_admin
from firebase_admin import credentials, firestore

biblioteca_routes = Blueprint('biblioteca_routes', __name__)

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@biblioteca_routes.route('/biblioteca/insert')
def test():
    db.collection('traduccion').add({
        'email': 'marcosvaldez@gmail.com',
        'idm_origen': 'eng',
        'idm_traduc': 'esp',
        'txt_origen': 'Dog',
        'txt_traduc': 'Perro',
        'imagen': 'link'
    })
    return "Traduccion insertada"