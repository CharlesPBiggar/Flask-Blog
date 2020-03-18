# Forms Page

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
                            validators=[DataRequired(), Regexp(regex=r'^[A-Za-z0-9\-\.]+@[A-Za-z\-]+.[a-z]{2,3}$', message='Not a valid Email.')])
                                                                        # Created Regular Expression to catch entrys that are not emails
    password = PasswordField('Password',
                            validators=[DataRequired(), Length(min=6, max=30)])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), Length(min=6, max=30), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose another username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already in use. Please choose another email or try signing in.')

class LoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired(), Length(min=6, max=30)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')