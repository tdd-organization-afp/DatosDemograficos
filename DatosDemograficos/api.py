from flask import Flask
from flask_restful import Resource, Api
import Datos.INE_tools as ine

app = Flask(__name__)
api = Api(app)

class BusquedaDatos(Resource):
	def get(self, filtro):
		return ine.INEDataBase(filtro)
        
api.add_resource(BusquedaDatos, '/<filtro>')

if __name__ == '__main__':
    app.run(debug=True)
