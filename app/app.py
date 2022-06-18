from flask import Flask
from BibliotecaTest.bibliotecaController import biblioteca_routes
app = Flask(__name__)

app.register_blueprint(biblioteca_routes)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True, port = 4000)
