from flask import Flask, render_template, request
from scraping import scrape
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    def post(self):
        return render_template("index.html")


api.add_resource(Hello, '/hello')



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)