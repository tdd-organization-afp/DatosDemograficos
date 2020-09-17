# URL de acceso a la información Total/Hombres/Mujeres de las provincias españolas
URL_POBLACION = "https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/9687?nult=1"

# El orden de las provincias en el INE y en el geojson están en diferente orden.
# Mediante este array podemos hacer la tradcucción INE->geojson
TRADUCTOR = [   12,    # Albacete
		32,	# Alicante
		 0,	# Almería 
		45,	# Álava
		48,	# Asturias
		17,	# Ávila
		35,	# Badajoz
		41,	# Islas Baleares
		26,	# Barcelona
		47,	# Vizcaya
		18, 	# Burgos
		36,	# Cácerees
		 1, 	# Cádiz
		11,	# Cantabria
		33,	# Castellón
		13,	# Ciudad Real
		 2,	# Códoba
		37,	# A coruña
		14,	# Cuenca
		46,	# Gipúzcoa
		27,	# Gerona
		 3,	# Granada
		15, 	# Guadalajara
		 4,	# Huelva
		 8, 	# Huesca
		 5,	# Jaén
		19, 	# León
		28,	# Lérida
		38, 	# Lugo
		30,	# Madrid
		 6,	# Málaga
		49,	# Murcia
		31,	# Navarra
		39,	# Ourense
		20,	# Palencia
		42,	# Las Palmas
		40,	# Pontevedra
		44,	# La Rioja
		21,	# Salamanca
		43,	# Santa Cruz de Tenerife
		22,	# Segovia
		 7,	# Sevilla
		23,	# Soria
		29,	# Tarragona
		 9,	# Teruel
		16,	# Toledo
		34,	# Valencia
		24,	# Valladolid
		25,	# Zamora
		10	# Zaragoza
		]

# La información proporcionada por el INE viene, por cada provincia, seguidos los datos de la población total, hombres y mujeres.
# Por tanto, tenemos que hacer incrementos de tres en tres para acceder a la misma información
INCREMENTO = 3
INI_INFO_TOTAL = 3 # Comienzo de la información 3-> Total. Albacete
		    #				  4-> Hombres. Albacete
		    #				  5-> Mujeres. Albacete
		    #				  6-> Total. Alicante ....
FIN_INFO_TOTAL = 151

	
