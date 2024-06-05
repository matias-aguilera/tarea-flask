# -*- coding: utf-8 -*-
from random import choice, shuffle
from flask import Flask
from flask.templating import render_template
import json
import os
app = Flask(__name__)




# Ruta principal
@app.route('/')
def index():
    with open("data/pokemon.json", "r", encoding="utf-8") as f:
        datos= json.load(f)
    return render_template('index.html', datos=datos)

# Ruta para mostrar un mensaje personalizado
@app.route('/saludo')
def saludar():
    return render_template('saludo.html')


# Ruta para mostrar una página de contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)

