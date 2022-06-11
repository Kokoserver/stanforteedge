from starlette_wtf import StarletteForm
from wtforms import StringField, PasswordField, PasswordField, ValidationError
from wtforms.widgets import PasswordInput
from wtforms.validators import DataRequired, Email, EqualTo

# user model
from stanforteedge.src.app.auth import models


class RegisterForm(StarletteForm):
    email = StringField(
        'Email address',
        validators=[
            DataRequired('Please enter your email address'),
            Email()
        ]
    )
    username = StringField(
        'username',
        validators=[
            DataRequired('Please enter your username'),
        ]
    )

    password = PasswordField(
        'Password',
        widget=PasswordInput(hide_value=False),
        validators=[
            DataRequired('Please enter your password'),
            EqualTo('confirm_password', message='Passwords must match')
        ]
    )

    confirm_password= PasswordField(
        'Confirm Password',
        widget=PasswordInput(hide_value=False),
        validators=[
            DataRequired('Please confirm your password')
        ]
    )

    async def async_validate_email(self, field):
        """Asynchronous validator to check if email is already in-use
        """
        check_user = await models.User.get_or_none(email = field.email)
        # replace this with your own code
        if check_user():
            raise ValidationError('account with this email already exists')

    async def async_validate_username(self, field):
        """Asynchronous validator to check if email is already in-use
        """
        check_user = await models.User.get_or_none(username = field.username)
        # replace this with your own code
        if check_user():
            raise ValidationError('account with this email already exists')



class LoginForm(StarletteForm):
    email = StringField(
        'Email address',
        validators=[
            DataRequired('Please enter your email address'),
            Email()
        ]
    )

    password = PasswordField(
        'Password',
        widget=PasswordInput(hide_value=False),
        validators=[
            DataRequired('Please enter your password'),
        
        ]
    )


    async def async_validate_email(self, field):
        """Asynchronous validator to check if email is already in-use
        """
        check_user = await models.User.get_or_none(email = field.email)
        # replace this with your own code
        if not check_user():
            raise ValidationError('account does not exist')

   
class ForgotPasswordForm(StarletteForm):
    email = StringField(
        'Email address',
        validators=[
            DataRequired('Please enter your email address'),
            Email()
        ]
    )


    async def async_validate_email(self, field):
        """Asynchronous validator to check if email is already in-use
        """
        check_user = await models.User.get_or_none(email = field.email)
        # replace this with your own code
        if not check_user():
            raise ValidationError('account does not exist')

   
class PasswordResetForm(StarletteForm):
    password = PasswordField(
        'Password',
        widget=PasswordInput(hide_value=False),
        validators=[
            DataRequired('Please enter your password'),
            EqualTo('confirm_password', message='Passwords must match')
        ]
    )

    confirm_password= PasswordField(
        'Confirm Password',
        widget=PasswordInput(hide_value=False),
        validators=[
            DataRequired('Please confirm your password')
        ]
    )

   