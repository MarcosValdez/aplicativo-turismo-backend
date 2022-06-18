from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
app = Flask(__name__)

class biblioteca():
    def test(self, db):
        try:
            db.collection('traduccion').add({
                'email': 'ortegachavez@gmail.com',
                'idm_origen': 'eng',
                'idm_traduc': 'esp',
                'txt_origen': 'Hello',
                'txt_traduc': 'Hola',
                'imagen': 'link'
            })
        except Exception as e: 
            print(f'Exception: {e}')

        return "Traducción insertada"