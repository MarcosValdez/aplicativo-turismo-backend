from flask import Flask, render_template,jsonify
import firebase_admin
from firebase_admin import credentials, firestore

from biblioteca import biblioteca

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
app = Flask(__name__)

bibClass = biblioteca

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/biblioteca', methods=['GET'])
def test():
    bibClass.test(db)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')



if __name__ == '__main__':
    app.run(debug=True, port = 4000)

