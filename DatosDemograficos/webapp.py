from flask import Flask, redirect, url_for, render_template, current_app
import requests
import json
from Datos.settings import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	current_app.logger.info('Mostrando la portada de la aplicación')
	#Añadir formulario con los filtros de búsqueda
	return render_template('index.html')
	#return redirect(url_for('buscar', name="filtro"))
    
@app.route('/<name>')
def map(name):
    info = requests.get('http://localhost:5000/'+name)
    jsonInfo = json.loads(info.text)
    
    if(jsonInfo == TOTAL_POB_MAPA):
        current_app.logger.info('Mostrando mapa del total de la población')
        return render_template('total_pob_mapa.html')
    elif (jsonInfo == HOMBRE_POB_MAPA):
    	current_app.logger.info('Mostrando mapa de la población de hombres')
    	return render_template('hombre_pob_mapa.html')
    elif (jsonInfo == MUJER_POB_MAPA):
    	current_app.logger.info('Mostrando mapa de la población de mujeres')
    	return render_template('mujer_pob_mapa.html')
    elif (jsonInfo == TOTAL_POB_BAR):
    	current_app.logger.info('Mostrando un gráfico de barras del total de la población')
    	return render_template('total_pob_bar.html')
    elif (jsonInfo == HOMBRE_POB_BAR):
    	current_app.logger.info('Mostrando un gráfico de barras de la población de hombres')
    	return render_template('hombre_pob_bar.html')
    elif (jsonInfo == MUJER_POB_BAR):
    	current_app.logger.info('Mostrando un gráfico de barras de la población de mujeres')
    	return render_template('mujer_pob_bar.html')
    elif (jsonInfo == AMBOS_POB_BAR):
    	current_app.logger.info('Mostrando un gráfico de barras de hombres/mujeres')
    	return render_template('ambos_pob_bar.html')
    else:
    	current_app.logger.info('Búsqueda no válida')
    	return render_template('non_valid.html')
    
if __name__ == '__main__':
    app.run(debug=True, port=5001)
