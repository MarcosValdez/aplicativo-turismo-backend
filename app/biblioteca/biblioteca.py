from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
app = Flask(__name__)

class bilioteca:
    def test(self, db):
        db.collection('traduccion').add({
            'email': 'ortegachavez@gmail.com',
            'idm_origen': 'eng',
            'idm_traduc': 'esp',
            'txt_origen': 'Hello',
            'txt_traduc': 'Hola',
            'imagen': 'link'
        })
        return "Traduccion insertada"