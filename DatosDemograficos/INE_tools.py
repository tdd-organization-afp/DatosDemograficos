import requests
import json
import matplotlib
import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from settings import *
		 
def INEDataBase(filtro):
	# Obtenemos la información de la URL
	try:
		info = requests.get(URL_POBLACION)
		jsonInfo = json.loads(info.text)
	
		# Nos quedamos con la población total en cada provincia
		poblacion = []
		for i in range(INI_INFO_TOTAL, FIN_INFO_TOTAL, INCREMENTO):
			poblacion.append(jsonInfo[i]["Data"][0]["Valor"] / 100000.0)

		# Leemos el geojson e incluimos la nueva columna
		m = "geojson/spain-provinces.geojson"
		map_data = gpd.read_file(m)
		map_data['POB2020'] = 0.0
		
		# Incluimos la información
		for i in range(len(TRADUCTOR)):
			map_data.loc[TRADUCTOR[i],'POB2020'] = poblacion[i]
		
		#Dibujamos el mapa
		fig, ax = plt.subplots(1, 1, figsize=(10, 10)) 
		# Control del encuadre (área geográfica) del mapa
		ax.axis([-12, 5, 32, 48])
		# Control del título y los ejes
		ax.set_title('Población total por provincias en 2020 (en 100 000 habitantes)', 
			     pad = 20, 
			     fontdict={'fontsize':20, 'color': '#4873ab'})
		ax.set_xlabel('Longitud')
		ax.set_ylabel('Latitud')
		 
		# Añadir la leyenda separada del mapa
		divider = make_axes_locatable(ax)
		cax = divider.append_axes("right", size="5%", pad=0.2)
		 
		# Generar y cargar el mapa
		map_data.plot(column='POB2020', cmap='plasma', ax=ax,
			      legend=True, cax=cax, zorder=5)
		print("HOlaaa")
		plt.savefig("fig/total_pob.png")
		
		return {"Mapa guardado con éxito. Búsqueda por":filtro}
		
	except requests.exceptions.RequestException as e: 
    		raise SystemExit(e)

	
