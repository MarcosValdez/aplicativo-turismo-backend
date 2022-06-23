from flask import Blueprint, render_template

from src.utils import connect_database

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
