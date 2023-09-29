from flask import Flask
from flask_restful import Api
from models import db
from views.user_view import User, UserList
from views.home_view import Home
from views.login_view import Login
from views.area_view import Area, AreaList
from views.to_do_view import Todo, TodoList
from views.vegetable_manager_view import VegetableManager, VegetableManagerList
from views.vegetable_infos_view import VegetableInfos, VegetableInfosList
from views.sensors_view import Sensor, SensorList, SensorsLast
from views.automation_view import AutomationList
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)


GREENHOUSE_MYSQL_USER = 'greenhouse_dev'
GREENHOUSE_MYSQL_PWD = 'AVNS_I6mOdk372jRm8stpS0d'
GREENHOUSE_MYSQL_HOST = 'db-mysql-ams3-26566-do-user-14634177-0.b.db.ondigitalocean.com'
GREENHOUSE_MYSQL_DB = 'greenhouse_db'
GREENHOUSE_MYSQL_PORT = 25060

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(GREENHOUSE_MYSQL_USER, GREENHOUSE_MYSQL_PWD, GREENHOUSE_MYSQL_HOST, GREENHOUSE_MYSQL_PORT, GREENHOUSE_MYSQL_DB)

db.init_app(app)
CORS(app)


api.add_resource(User, '/users/<string:user_id>')
api.add_resource(UserList, '/users')

api.add_resource(Area, '/areas/<string:area_id>')
api.add_resource(AreaList, '/areas')

api.add_resource(Sensor, '/sensors/<string:sensor_id>')
api.add_resource(SensorList, '/sensors')
api.add_resource(SensorsLast, '/sensors/last')
api.add_resource(AutomationList, '/automation')

api.add_resource(VegetableManager, '/vegetable_manager/<string:vegetable_id>')
api.add_resource(VegetableManagerList, '/vegetable_manager')

api.add_resource(VegetableInfos, '/vegetable_infos/<string:vegetable_id>')
api.add_resource(VegetableInfosList, '/vegetable_infos')

api.add_resource(Todo, '/todo/<string:todo_id>')
api.add_resource(TodoList, '/todo')

# api.add_resource(Login, '/login')

api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
