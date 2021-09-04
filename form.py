from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, PasswordField
from wtforms.fields.html5 import EmailField

class FormRegister(Form):
    # 依照 Model 建置相對應的 Form
    # password2：確認密碼
    username = StringField('使用者名稱', validators=[validators.DataRequired(), validators.Length(10, 30)])
    email = EmailField('Email', validators=[validators.DataRequired(), validators.Length(1, 50), validators.Email()])
    password = PasswordField('密碼', validators=[validators.DataRequired(), validators.Length(5, 10), validators.EqualTo('password2', message='密碼須符合')])
    password2 = PasswordField('確認密碼', validators=[validators.DataRequired()])
    submit = SubmitField('註冊')
    