from flask import Flask, jsonify
from flask_restful import Resource, Api
from API import api_one, api_two, api_three

app = Flask(__name__)
api = Api(app)

api.add_resource(api_one.Add, "/add")
api.add_resource(api_two.Date, "/get_date")
api.add_resource(api_three.Chat, "/chat")

if __name__ == '__main__':
    app.run(debug=True)
