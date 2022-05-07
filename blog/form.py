# Standard imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.simple import BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
            validators=[DataRequired(), Length(min=8, max=15)])
    confirm_password = PasswordField('Password',
            validators=[DataRequired(), Length(min=8, max=15), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
            validators=[DataRequired(), Length(min=8, max=15)])
    remember = BooleanField('Remember Me')
    login = SubmitField('Login')
