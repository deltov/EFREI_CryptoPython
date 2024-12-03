from cryptography.fernet import Fernet
from flask import Flask, rendertemplatestring, rendertemplate, jsonify
from flask import rendertemplate
from flask import json
from urllib.request import urlopen
import sqlite3

app = Flask(name)

@app.route('/')
def hello_world():
    return render_template('hello.html') 

key = Fernet.generate_key() #sss
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        token_bytes = token.encode()  # Conversion str -> bytes
        valeur = f.decrypt(token_bytes)  # Décrypte le token
        return f"Valeur décryptée : {valeur.decode()}"  # Retourne la valeur en str
    except Exception as e:
        return f"Erreur de décryptage : {str(e)}"

if __name == "__main":
  app.run(debug=True)
