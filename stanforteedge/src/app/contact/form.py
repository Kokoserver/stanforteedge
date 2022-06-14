from starlette_wtf import StarletteForm
from wtforms import StringField, TextAreaField
from wtforms.widgets import  TextArea
from wtforms.validators import DataRequired, Email




class ContactForm(StarletteForm):
    email = StringField(
        'Email address',
        validators=[
            DataRequired('Please enter your email address'),
            Email()
        ]
    )
    full_name = StringField(
        'full name',
        validators=[
            DataRequired('Please enter your full name'),
        ]
    )
    message = TextAreaField(label="message", widget=TextArea())


