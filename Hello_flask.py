from flask import Flask
from flask import render_template
from flask import url_for
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello Flask"

@app.route("/apple")
def apple():
    return "I am apple!"

@app.route("/add/num1=<num1>&num2=<num2>", methods=['GET'])
def add(num1, num2):
    print(num1 + num2)
    return str(int(num1) + int(num2))

@app.route('/')
def index():
    return render_template(r"index.html")

@app.route('/user/<username>')
def username(username):
    return "I am " + username

@app.route("/age/<int:age>")
def userage(age):
    return "I am " + str(age) + " years old"

@app.route('/a')
def url_for_a():
    return "here is a"

@app.route("/b")
def b():
    return redirect(url_for('url_for_a'))

if __name__ == "__main__":
    app.run()