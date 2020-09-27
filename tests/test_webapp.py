import pytest

from ..DatosDemograficos.Datos import settings
from ..DatosDemograficos.Datos import INE_tools

# Tests para comprobar que los mapas y las gráficas se generan de forma correcta
def test_totalPobMapa(requests_mock):
	requests_mock.get(settings.URL_POBLACION, json= settings.MOCK_GET)
	ine = INE_tools.INE()
	info = ine.totalPobMapa()
	assert info == "Mapa del total de la población generado correctamente."
	
def test_homPobMapa(requests_mock):
	requests_mock.get(settings.URL_POBLACION, json= settings.MOCK_GET)
	ine = INE_tools.INE()
	info = ine.homPobMapa()
	assert info == "Mapa del total de hombres generado correctamente."
	
def test_mujPobMapa(requests_mock):
	requests_mock.get(settings.URL_POBLACION, json= settings.MOCK_GET)
	ine = INE_tools.INE()
	info = ine.mujPobMapa()
	assert info == "Mapa del total de mujeres generado correctamente."
	
def test_totalPobBar(requests_mock):
	requests_mock.get(settings.URL_POBLACION, json= settings.MOCK_GET)
	ine = INE_tools.INE()
	info = ine.totalPobBar()
	assert info == "Gráfico de barras del total de la población generado correctamente."
	
def test_homPobBar(requests_mock):
	requests_mock.get(settings.URL_POBLACION, json= settings.MOCK_GET)
	ine = INE_tools.INE()
	info = ine.homPobBar()
	assert info == "Gráfico de barras de hombres generado correctamente."
	
def test_mujPobBar(requests_mock):
	requests_mock.get(settings.URL_POBLACION, json= settings.MOCK_GET)
	ine = INE_tools.INE()
	info = ine.mujPobBar()
	assert info == "Gráfico de barras de mujeres generado correctamente."
	
def test_ambosPobBar(requests_mock):
	requests_mock.get(settings.URL_POBLACION, json= settings.MOCK_GET)
	ine = INE_tools.INE()
	info = ine.ambosPobBar()
	assert info == "Gráfico de barras de hombres y mujeres generado correctamente."
	
def test_error(requests_mock):
	requests_mock.get(settings.URL_POBLACION, json= settings.MOCK_GET)
	ine = INE_tools.INE()
	info = ine.INEDataBase("asdasd")
	assert info == "non_valid"
