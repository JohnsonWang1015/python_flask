from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email

from view_form import UserForm

app = Flask(__name__)
Bootstrap(app)

@app.route('/user', methods=['GET', 'POST'])
def user():
    form = UserForm()
    if form.validate_on_submit():
        return "Success Submit"
    return render_template('user.html', form=form)

if __name__ == "__main__":
    app.debug = True
    app.config['SECRET_KEY'] = '12345'
    app.run()