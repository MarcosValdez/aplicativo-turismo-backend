from flask import Blueprint, jsonify
from src.utils.db import connect_database
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import easyocr

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
