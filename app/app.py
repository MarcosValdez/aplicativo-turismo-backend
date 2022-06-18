from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

from biblioteca import biblioteca

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
app = Flask(__name__)

bibClass = biblioteca

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/biblioteca', methods=['GET'])
def test():
    biblioteca.test(db)

if __name__ == '__main__':
    app.run(debug=True, port = 4000)

