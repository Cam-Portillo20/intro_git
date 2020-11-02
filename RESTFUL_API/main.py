from flask import Flask,jsonify
from conexion import get_usuarios

app = Flask(__name__)

@app.route("/")

def hola():
    return "Hola Mundo!"

@app.route("/api/v1/usuarios")
def usuarios():
    usuarios_list = get_usuarios()
    return jsonify(usuarios_list)

app.run()
