from flask import Flask
from flask import render_template
from flask import make_response
from flask import Response
import json

from flask.json import jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/api/test1", methods=['GET'])
def test_api():
    return jsonify(message="Hello, API")

@app.route("/api/test2", methods=['GET'])
def test_api2():
    resp = make_response(json.dumps(dict(message="Hello, API2")))
    resp.headers['Content-Type'] = 'application/json;charset=UTF-8'
    return resp

@app.route("/api/test3")
def test_api3():
    return Response(json.dumps({"message":"Hello, API3"}), mimetype="application/json")

if __name__ == "__main__":
    app.debug = True
    app.run() 