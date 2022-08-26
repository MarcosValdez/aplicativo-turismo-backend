"""Prepare data for Plotly Dash."""
from cmath import nan
import numpy as np
import pandas as pd
from src.utils.db import connect_database
from flask import jsonify, make_response

db = connect_database()

def create_dataframe():
    paises = []
    datos = db.collection('users').stream()
    for doc in datos:
        nuevo = doc.to_dict()
        nuevo['doc_id'] = doc.id
        paises.append(nuevo)
    
    df = pd.json_normalize(paises)
    return df
"""    
    print(maximos)
    data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    } """
    
