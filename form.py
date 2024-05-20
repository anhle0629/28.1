from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class AddPetForm (FlaskForm):
    name = StringField("Name", validator= [InputRequired(message = "Pet need a name")])

    speices = StringField("Speices", validators=[InputRequired(message="What is the spieces?")])

    photo = StringField("Photo", validators=[Optional(), URL()])

    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max= 20)])

    note = TextAreaField("Note", validators=[Optional(), Length(min=10)])

class EditPetForm (FlaskForm):
    photo_url = StringField("photo", validators=[Optional(), URL()])

    note = TextAreaField("Note", validators=[Optional(), Length(min=10)])

    available = BooleanField("Available?")



