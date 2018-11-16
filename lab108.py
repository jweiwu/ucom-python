# encoding=UTF-8
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Rest1(Resource):
    def get(self):
        return {"key1": "Hello world", "key2": "Mark Ho"}


class Rest2(Resource):
    def get(self):
        return ['Mark', 'john', '恆逸資訊', '程式設計']


api.add_resource(Rest1, '/rest1')
api.add_resource(Rest2, '/rest2')
app.run(port=5551, host='0.0.0.0', debug=True)
