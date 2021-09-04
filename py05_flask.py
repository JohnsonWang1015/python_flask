from flask import Flask
from flask import render_template
from flask import url_for
from werkzeug.utils import redirect
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/loginurl', methods=["GET", 'POST'])
def login():
    if request.method == "POST":
        return redirect(url_for('hello', username=request.form.get('username')))
    else:
        return render_template('login.html')

@app.route("/hello/<username>")
def hello(username):
    return render_template('hello.html', username=username)

if __name__ == "__main__":
    app.debug = True
    app.run()