from src.utils.db import connect_database
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

conteo = Blueprint('conteo', __name__)
db = connect_database()

@cross_origin
@conteo.route("/contar_ingles/<string:sentence>",methods=['POST'])
def contar_palabras_ingles(sentence):
    try:
        data = request.json
        diccionario_frecuencias = contar(data['palabra'])
        for palabra in diccionario_frecuencias:
            nuevo = {
                'palabra': palabra,
                'frecuencia': diccionario_frecuencias[palabra]
            }
            conteo_ref = db.collection('conteo_ingles').document(nuevo['palabra']).get()
            if conteo_ref.exists:
                frecuencia_nueva = conteo_ref.to_dict()["frecuencia"] + nuevo['frecuencia']
                db.collection('conteo_ingles').document(nuevo['palabra']).update({
                    'palabra': nuevo['palabra'],
                    'frecuencia': frecuencia_nueva
                })
            else:
                db.collection('conteo_ingles').document(nuevo['palabra']).set(nuevo)
        return jsonify("Exito"), 200
    except Exception as e:
        return jsonify({
            'error': f'Exception: {e}'
        }), 400

@cross_origin
@conteo.route("/contar_espanol/<string:sentence>",methods=['POST'])
def contar_palabras_espanol(sentence):
    
    diccionario_frecuencias = contar(sentence)

    for palabra in diccionario_frecuencias:
        nuevo = {
            'palabra': palabra,
            'frecuencia': diccionario_frecuencias[palabra]
        }
        conteo_ref = db.collection('conteo_espanol').document(nuevo['palabra']).get()
        if conteo_ref.exists:
            frecuencia_nueva = conteo_ref.to_dict()["frecuencia"] + nuevo['frecuencia']
            db.collection('conteo_espanol').document(nuevo['palabra']).update({
                'palabra': nuevo['palabra'],
                'frecuencia': frecuencia_nueva
            })
        else:
            db.collection('conteo_espanol').document(nuevo['palabra']).set(nuevo)
    return jsonify("Exito"), 200

def contar(sentence):
    quitar = ".,;:\n!\"'%"
    for caracter in quitar:
        sentence = sentence.replace(caracter,"")

    sentence = sentence.lower()
    palabras = sentence.split(" ")

    diccionario_frecuencias = {}
    for palabra in palabras:
        if palabra in diccionario_frecuencias:
            diccionario_frecuencias[palabra] += 1
        else:
            diccionario_frecuencias[palabra] = 1
    return diccionario_frecuencias