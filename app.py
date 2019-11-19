from flask import Flask, render_template, request, send_from_directory
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class Ola(Resource):
    def get(self):
        return render_template("ola.html")

api.add_resource(Hello, '/hello')

@app.route('/')
def index():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)