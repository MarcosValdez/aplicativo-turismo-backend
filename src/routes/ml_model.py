from flask import Blueprint, jsonify
from src.utils.db import connect_database
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import easyocr
from flask_cors import cross_origin

ml_model = Blueprint('ml_model', __name__)
db = connect_database()

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-es-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-es-en")
reader = easyocr.Reader(['es'])


@ml_model.route("/translate/<string:sentence>")
def translate(sentence):
    batch = tokenizer([sentence], return_tensors="pt")
    generated_ids = model.generate(**batch)
    resultado = tokenizer.batch_decode(
        generated_ids, skip_special_tokens=True)[0]
    return jsonify({'original': sentence, 'traducido': resultado}), 200


@ml_model.route("/image2text/<string:path>")
def image2text(path):
    IMAGE_PATH = f'./src/static/{path}.jpg'
    result = reader.readtext(IMAGE_PATH)
    final_result = ''
    for detection in result:
        final_result += detection[1]
        final_result += ' '
    return jsonify({'res': final_result}), 200


@ml_model.route("/translateimage/<string:path>")
def translateimage(path):
    IMAGE_PATH = f'./src/static/{path}.jpg'
    result = reader.readtext(IMAGE_PATH)
    final_result = ''
    for detection in result:
        final_result += detection[1]
        final_result += ' '
    batch = tokenizer([final_result], return_tensors="pt")
    generated_ids = model.generate(**batch)
    resultado = tokenizer.batch_decode(
        generated_ids, skip_special_tokens=True)[0]
    return jsonify({'original': final_result, 'traducido': resultado}), 200

@cross_origin
@ml_model.route("/contar_ingles/<string:sentence>")
def contar_palabras_ingles(sentence):
    try:
        diccionario_frecuencias = conteo(sentence)
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
@ml_model.route("/contar_espanol/<string:sentence>")
def contar_palabras_espanol(sentence):
    
    diccionario_frecuencias = conteo(sentence)

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

def conteo(sentence):
    quitar = ".,;:\n!\"'"
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