import pytest
import threading

from ..DatosDemograficos.Datos import INE_tools
from ..DatosDemograficos.Datos import geojson
from ..DatosDemograficos.Datos import static
from ..DatosDemograficos.Datos import settings
import webapp
import api

PREFIJO = "Datos/"
PREFIJO2 = "Datos/static/"
subprocesos = []

@pytest.fixture
def client():
    webapp.app.config['TESTING'] = True
    api.app.config['TESTING'] = True
    
    # Iniciamos el servidor
    thread = threading.Thread(target=api.app.run)
    thread.daemon = True # Para que acabe con el padre
    thread.start()

    
    with webapp.app.test_client() as client:
        yield client

    
@pytest.mark.integration_test
def test_home(client):
	rv = client.get("/")
	assert rv.status_code == 302

@pytest.mark.integration_test
def test_totalPobMapa(client):
	rv = client.get("/" + settings.TOTAL_POB_MAPA)
	assert rv.status_code == 200
	
@pytest.mark.integration_test	
def test_homPobMapa(client):
	rv = client.get("/" + settings.HOMBRE_POB_MAPA)
	assert rv.status_code == 200
	
@pytest.mark.integration_test	
def test_mujPobMapa(client):
	rv = client.get("/" + settings.MUJER_POB_MAPA)
	assert rv.status_code == 200
	
@pytest.mark.integration_test	
def test_totalPobBar(client):
	rv = client.get("/" + settings.TOTAL_POB_BAR)
	assert rv.status_code == 200
	
@pytest.mark.integration_test	
def test_homPobBar(client):
	rv = client.get("/" + settings.HOMBRE_POB_BAR)
	assert rv.status_code == 200
	
@pytest.mark.integration_test	
def test_mujPobBar(client):
	rv = client.get("/" + settings.MUJER_POB_BAR)
	assert rv.status_code == 200
	
@pytest.mark.integration_test	
def test_ambosPobBar(client):
	rv = client.get("/" + settings.AMBOS_POB_BAR)
	assert rv.status_code == 200
