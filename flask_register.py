from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

import os
import pymssql

app = Flask(__name__)

# 預設 None 會有異常
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 設置資料庫為 MS-SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://sa:12345@localhost:1433/demo1'

app.config['SECRET_KEY'] = os.urandom(10)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    from form import FormRegister
    from model import UserRegister
    
    form = FormRegister()
    if form.validate_on_submit():
        #return "成功了，謝謝支持"
        user = UserRegister(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data        
        )
        db.session.add(user)
        db.session.commit()
        return "成功了，謝謝支持"
    return render_template('register.html', form=form)
    
if __name__ == "__main__":
    app.debug = True
    app.run()