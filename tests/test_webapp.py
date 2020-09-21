import pytest

#from DatosDemograficos import settings
from ..DatosDemograficos.Datos import INE_tools
from ..DatosDemograficos.Datos import geojson
from ..DatosDemograficos.Datos import static

PREFIJO = "DatosDemograficos/Datos/"
PREFIJO2 = "DatosDemograficos/Datos/static/"

# Tests para comprobar que los mapas y las gráficas se generan de forma correcta

def test_totalPobMapa():
	info = INE_tools.totalPobMapa(PREFIJO, PREFIJO2)
	assert info == "Mapa del total de la población generado correctamente."
	
def test_homPobMapa():
	info = INE_tools.homPobMapa(PREFIJO, PREFIJO2)
	assert info == "Mapa del total de hombres generado correctamente."
	
def test_mujPobMapa():
	info = INE_tools.mujPobMapa(PREFIJO, PREFIJO2)
	assert info == "Mapa del total de mujeres generado correctamente."
	
def test_totalPobBar():
	info = INE_tools.totalPobBar(PREFIJO2)
	assert info == "Gráfico de barras del total de la población generado correctamente."
	
def test_homPobBar():
	info = INE_tools.homPobBar(PREFIJO2)
	assert info == "Gráfico de barras de hombres generado correctamente."
	
def test_mujPobBar():
	info = INE_tools.mujPobBar(PREFIJO2)
	assert info == "Gráfico de barras de mujeres generado correctamente."
	
def test_ambosPobBar():
	info = INE_tools.ambosPobBar(PREFIJO2)
	assert info == "Gráfico de barras de hombres y mujeres generado correctamente."
	
def test_error():
	info = INE_tools.INEDataBase("asdasd")
	assert info == "non_valid"
