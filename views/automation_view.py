from flask import jsonify
from flask_restful import Resource, fields, marshal_with, reqparse
from models import db
from utils import abort_if_doesnt_exist
from models.sensors_model import AutomationModel

resource_fields = {
    'id': fields.String,
    'air_humidity_selection': fields.Integer,
    'air_temperature_selection': fields.Integer,
    'water_pump_left_state': fields.Boolean,
    'water_pump_left_timer': fields.Integer,
    'water_pump_middle_state': fields.Boolean,
    'water_pump_middle_timer': fields.Integer,
    'water_pump_right_state': fields.Boolean,
    'water_pump_right_timer': fields.Integer
}

class AutomationList(Resource):
    @marshal_with(resource_fields)
    def get(self):
        selections = AutomationModel.query.all()
        return selections

    @marshal_with(resource_fields)
    def post(self):
        parser_create = reqparse.RequestParser()

        # Define a list of argument names and their types
        argument_list = [
            ('air_humidity_selection', int, None, False),
            ('air_temperature_selection', int, None, False),
            ('water_pump_left_state', bool, None, False),
            ('water_pump_left_timer', int, None, False),
            ('water_pump_middle_state', bool, None, False),
            ('water_pump_middle_timer', int, None, False),
            ('water_pump_right_state', bool, None, False),
            ('water_pump_right_timer', int, None, False)
        ]

        # Iterate through the argument list and add arguments to the parser
        for arg_name, arg_type, arg_help, arg_required in argument_list:
            parser_create.add_argument(
                arg_name, 
                type=arg_type, 
                help=arg_help,
                required=arg_required
            )

        args = parser_create.parse_args()

        # Create the AutomationModel object using the arguments
        new_selection = AutomationModel(**args)
        
        db.session.add(new_selection)
        db.session.commit()
        
        return new_selection, 201
