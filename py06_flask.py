from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask import flash

import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/loginurl', methods=["GET", 'POST'])
def login():
    if request.method == "POST":
        if login_check(request.form['username'], request.form['password']):
            flash('Login Success')
            return redirect(url_for('hello', username=request.form.get('username')))
    else:
        return render_template('form.html')

def login_check(username, password):
    if username == "admin" and password == "hello":
        return True
    else:
        return False

@app.route("/hello/<username>")
def hello(username):
    return render_template('hello.html', username=username)

if __name__ == "__main__":
    app.debug = True
    app.secret_key = os.urandom(5)
    print(app.secret_key)
    app.run()