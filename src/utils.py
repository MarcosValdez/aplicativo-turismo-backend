from firebase_admin import credentials, firestore
import firebase_admin

cred = credentials.Certificate("./src/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def connect_database():
    return db