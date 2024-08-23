from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',page='index')

@app.route('/mision.html')
def mision():
    return render_template('mision.html',page='mision')

@app.route('/vision.html')
def vision():
    return render_template('vision.html',page='vision')

@app.route('/contacto.html')
def contacto():
    return render_template('contacto.html',page='contacto')

@app.route('/index.html')
def home():
    return render_template('index.html',page='index')