from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import EmailField
#  引入驗證
from wtforms.validators import DataRequired, Email

class UserForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired(message='Not Null')])
    email = EmailField('Email', validators=[DataRequired(message='Not Null')])
    submit = SubmitField('Submit')