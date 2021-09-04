from flask import Flask
from flask import render_template
from flask.json import jsonify
from flask.views import MethodView


app = Flask(__name__)

class API_Test(MethodView):
    def get(self):
        return jsonify(message="I am GET")
    def post(self):
        return jsonify(message="I am POST")
    def delete(self):
        return jsonify(message="I am DELETE")

@app.route("/")
def index():
    return render_template('home.html')

app.add_url_rule('/api/test', view_func=API_Test.as_view("test_api"))

if __name__ == "__main__":
    app.debug = True
    app.run()