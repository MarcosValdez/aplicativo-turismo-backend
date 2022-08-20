from datetime import datetime
from flask import Blueprint, render_template

from src.utils.db import connect_database

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
    datos = []
    for doc in db.collection('task').stream():
        new_elem = doc.to_dict()
        # dt_obj = datetime.strptime(,
                                #    "%Y-%m-%d %H:%M:%S.%f")
        print(new_elem['date_created'].timestamp())
        # new_elem['date_created'] = datetime.datetime.strptime(new_elem['date_created'], '%Y/%m/%d')
        datos.append(new_elem)
    return render_template('dashboard.html', datos=datos)
