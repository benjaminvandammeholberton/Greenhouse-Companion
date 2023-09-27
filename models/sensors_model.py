from. import db
from models.base_model import BaseModel

class SensorsModel(BaseModel, db.Model):
    air_temperature = db.Column(db.Float)
    air_humidity = db.Column(db.Float)
    luminosity = db.Column(db.Float)

class AutomationModel(BaseModel, db.Model):
    air_humidity_selection = db.Column(db.Integer)
    air_temperature_selection = db.Column(db.Integer)
    water_pump_left_state = db.Column(db.Boolean)
    water_pump_left_timer = db.Column(db.Integer)
    water_pump_middle_state = db.Column(db.Boolean)
    water_pump_middle_timer = db.Column(db.Integer)
    water_pump_right_state = db.Column(db.Boolean)
    water_pump_right_timer = db.Column(db.Integer)
