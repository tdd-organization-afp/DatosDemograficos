from flask import Flask, request
from flask_restful import Resource, Api
import Datos.INE_tools as ine

app = Flask(__name__)
api = Api(app)

class BusquedaDatos(Resource):
	def __init__(self, ine_busqueda):
		self.ine_busqueda = ine_busqueda # !!!!!! INYECCIÓN/INVERSIÓN DE DEPENDENCIAS !!!!!!
		
	def get(self, filtro):
		return self.ine_busqueda.INEDataBase(filtro)
		
ine_busqueda = ine.INE()
api.add_resource(BusquedaDatos, '/<filtro>', resource_class_kwargs={'ine_busqueda': ine_busqueda})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
