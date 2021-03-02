from flask import Blueprint
from flask_restful import Api
from blueprint.api.resources import GetInfo, GetEvents

flask_api = Blueprint("api", __name__)
api = Api(flask_api)

api.add_resource(GetInfo, '/api/info')
api.add_resource(GetEvents, '/api/timeline')
