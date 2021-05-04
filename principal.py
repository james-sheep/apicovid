from flask import Flask, render_template
from flask import Flask
from consulta import busca_api

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/index', methods=['GET','POST'])
def index():
   
    contexto = busca_api('Aracaju')

    return render_template('index.html', context=contexto)

