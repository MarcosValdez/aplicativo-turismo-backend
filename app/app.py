from flask import Flask, render_template,jsonify
import firebase_admin
from firebase_admin import credentials, firestore

from biblioteca.biblioteca import biblioteca

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
app = Flask(__name__)

bibClass = biblioteca()

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/traducir', methods=['GET'])
def test():
    resp = bibClass.test(db)
    return jsonify({'msg': resp})

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/dashboard")
def dashboard():
    datos = bibClass.list(db)
    return render_template('dashboard.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True, port = 4000)

