from flask import Flask
from blueprint.api.main_api import flask_api
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from utility import get_data

app = Flask(__name__)
api = Api(app)

app.register_blueprint(flask_api)

if __name__ == '__main__':
    app.run(debug=True)
