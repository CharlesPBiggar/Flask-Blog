# Forms Page

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
                            validators=[DataRequired(), Regexp(regex='^[A-Za-z0-9\-\.]+@[A-Za-z\-]+.[a-z]{2,3}$', message='Not a valid Email.')])
                                                                        # Created Regular Expression to catch entrys that are not emails
    password = PasswordField('Password',
                            validators=[DataRequired(), Length(min=6, max=30)])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), Length(min=6, max=30), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired(), Length(min=6, max=30)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')