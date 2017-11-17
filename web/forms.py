from __future__ import absolute_import, division, print_function, unicode_literals

from flask_wtf import Form
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(Form):
    """Loging Form."""

    username = StringField(
        'Your username:',
        validators=[DataRequired(message="Please enter the Username")])
    password = PasswordField(
        'Password',
        validators=[DataRequired(message="Please enter the Password")])
    remember_me = BooleanField('Remember Me ')
    submit = SubmitField('Log In')
