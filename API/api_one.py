from flask_restful import Resource, request
from flask import jsonify


class Add(Resource):

    def post(self):
        res_dic = {}
        sum_key = []
        data = request.get_json()
        for list_k in data:
            for dic in data[list_k]:
                if dic.keys() in sum_key:
                    res_dic["result"] += sum(dic.values())
                else:
                    sum_key.append(dic.keys())
                    res_dic["result"] = sum(dic.values())

        return jsonify(res_dic)
