from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
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
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)

@app.route('/Exercice1')
def ex1():
    return render_template('exercice1.html') 

@app.route('/Exercice2')
def ex2():
    return render_template('exercice2.html') 

@app.route('/Exercice3')
def ex3():
    return render_template('exercice3.html') 

@app.route('/Exercice4')
def ex4():
    return render_template('exercice4.html') 

@app.route('/sommaire')
def som():
    return render_template('sommaire.html') 

@app.route('/accueil')
def acu():
    return render_template('accueil.html')
  
@app.route('/site')
def site():
    return render_template('site.html')

@app.route('/maison')
def maison():
    return render_template('maison.html')

@app.route('/baptiste')
def baptiste():
    return render_template('baptiste.svg')

@app.route('/chenille')
def chenille():
    return render_template('chenille.html')

@app.route('/dée')
def dée():
    return render_template('Jeu_Des_Base.html')
