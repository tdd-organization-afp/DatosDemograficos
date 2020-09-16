from flask import Flask, redirect, url_for
import requests


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	#Añadir formulario con los filtros de búsqueda
	return redirect(url_for('buscar', name="filtro"))
    
@app.route('/<name>')
def buscar(name):
    info = requests.get('http://localhost:5000/'+name)
    return info.text
    
if __name__ == '__main__':
    app.run(debug=True, port=5001)
