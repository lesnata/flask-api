import time
import datetime
from flask import Flask
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from utility import get_data


# listing all string parameters
parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('startDate',
                    type=str,
                    required=True,
                    help='Start date is not integer type')
parser.add_argument('endDate',
                    type=str,
                    required=True,
                    help='End date is not integer type')
parser.add_argument('type',
                    choices=["cumulative", "usual"],
                    default='usual',
                    help='Accepts only 2 values: "cumulative" or "usual"')
parser.add_argument('grouping',
                    choices=["weekly", "bi-weekly", "monthly"],
                    default='weekly',
                    help='Accepts only 3 values: "weekly", "bi-weekly" or "monthly"')
parser.add_argument('')


# importing json file with attributes
attributes = get_data("blueprint/api/attributes.json")
# attributes_structure = {
#     "startDate": fields.String,
#     "endDate": fields.String,
#     "type": fields.List,
#     "grouping": fields.List,
#     "asin": fields.String,
#     "brand": fields.String,
#     "source": fields.String,
#     "stars": fields.List
# }


class GetInfo(Resource):
    def get(self):
        '''
        GET /api/info
        Example:
        http://localhost:5000/api/info
        This method doesn’t require any parameters

        Returns: Information about possible filtering
        (list of attributes and list of values for each attribute)
        '''
        return attributes, 200


class GetEvents(Resource):
    def get(self):
        startDate = parser.parse_args(strict=True).get("startdate")
        endDate = parser.parse_args(strict=True).get("enddate")
        try:
            startDate_unix_epoch = time.mktime(datetime.datetime.strptime(startDate, "%Y-%m-%d").timetuple())
            endDate_unix_epoch = time.mktime(datetime.datetime.strptime(endDate, "%Y-%m-%d").timetuple())
        except TypeError:
            return Response("{} or {} is in wrong format".format(startDate, endDate), 400)



        data = []

        return {'timeline': 'data'}, 200
