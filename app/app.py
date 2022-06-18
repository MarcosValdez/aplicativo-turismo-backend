from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"