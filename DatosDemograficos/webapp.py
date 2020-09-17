from flask import Flask, redirect, url_for, render_template
import requests
import json
from settings import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	#Añadir formulario con los filtros de búsqueda
	return render_template('index.html')
	#return redirect(url_for('buscar', name="filtro"))
    
@app.route('/<name>')
def map(name):
    info = requests.get('http://localhost:5000/'+name)
    jsonInfo = json.loads(info.text)
    
    if(jsonInfo == TOTAL_POB_MAPA):
	    return render_template('total_pob_mapa.html')
    elif (jsonInfo == HOMBRE_POB_MAPA):
	    return render_template('hombre_pob_mapa.html')
    elif (jsonInfo == MUJER_POB_MAPA):
	    return render_template('mujer_pob_mapa.html')
    elif (jsonInfo == TOTAL_POB_BAR):
	    return render_template('total_pob_bar.html')
    elif (jsonInfo == HOMBRE_POB_BAR):
	    return render_template('hombre_pob_bar.html')
    elif (jsonInfo == MUJER_POB_BAR):
	    return render_template('mujer_pob_bar.html')
    elif (jsonInfo == AMBOS_POB_BAR):
	    return render_template('ambos_pob_bar.html')
    else:
        return render_template('non_valid.html')
    
if __name__ == '__main__':
    app.run(debug=True, port=5001)
