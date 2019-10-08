from flask import Flask
from flask import jsonify
from scraping import scrape
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('User-Agent', location='headers')
        args = parser.parse_args()
        return jsonify(data = scrape(args))

api.add_resource(Login, '/login')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)