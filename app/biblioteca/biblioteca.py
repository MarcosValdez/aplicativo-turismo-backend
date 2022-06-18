from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
app = Flask(__name__)

class biblioteca():
    def test(self, db):
        try:
            db.collection('traduccion').add({
                'email': 'nuevocorreo@gmail.com',
                'idm_origen': 'eng',
                'idm_traduc': 'esp',
                'txt_origen': 'texto',
                'txt_traduc': 'text',
                'imagen': 'http://'
            })
        except Exception as e: 
            print(f'Exception: {e}')

        return "Traducción insertada"
    
    def list(self, db):
        return [doc.to_dict() for doc in db.collection('traduccion').stream()]