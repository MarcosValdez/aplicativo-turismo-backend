from datetime import datetime
from flask import Blueprint, render_template
from src.utils.db import connect_database
import firebase_admin

views = Blueprint('views', __name__)

db = connect_database()


@views.route("/")
def home():
    return render_template('home.html')


@views.route("/login")
def login():
    return render_template('login.html')


@views.route("/dashboard")
def dashboard():
    return render_template('dashboard.html', datos=[doc.to_dict() for doc in db.collection('traduccion').stream()])

@views.route("/conteo")
def conteoingles():
    return render_template('conteo.html', 
            datosespanol=[doc.to_dict() for doc in db.collection('conteo_espanol').order_by("frecuencia", direction="DESCENDING").limit(8).stream()],
            datosingles=[doc.to_dict() for doc in db.collection('conteo_ingles').order_by("frecuencia", direction="DESCENDING").limit(8).stream()])
