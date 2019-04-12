from flask_restful import Resource, request
from flask import jsonify


class Chat(Resource):

    def post(self):
        res = {}
        msg_data = request.get_json()
        if "您好" in msg_data["msg"] and "再见" in msg_data["msg"]:
            res["result"] = "天气不错"
        elif "再见" in msg_data["msg"]:
            res["result"] = "回见了您内。"
        elif "您好" in msg_data["msg"]:
            res["result"] = "您好, 您吃了吗?"
        return jsonify(res)
