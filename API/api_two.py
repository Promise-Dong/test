import datetime
from flask_restful import Resource
from flask import jsonify


class Date(Resource):

    def get(self):
        res = {}
        res["date"] = str(datetime.date.today())
        return jsonify(res)
