from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self, name):
        return {
            "message": "success",
            "data": "your name is " + name + ""
        }


api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
