from cryptography.fernet import Fernet
from flask import Flask, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3

app = Flask(__name__)

# Clé générée pour chiffrer et déchiffrer
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Route d'encryptage
@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

# Route de décryptage
@app.route('/decrypt/<string:valeur>')
def decryptage(valeur):
    try:
        valeur_bytes = valeur.encode()  # Conversion str -> bytes
        valeur_decryptee = f.decrypt(valeur_bytes).decode()  # Décryptage
        return f"Valeur décryptée : {valeur_decryptee}"  # Retourne la valeur décryptée en str
    except Exception as e:
        return f"Erreur lors du décryptage : {str(e)}"  # En cas d'erreur

if __name__ == "__main__":
    app.run(debug=True)
