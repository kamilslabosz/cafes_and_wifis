from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    img_url = StringField("Cafe image (URL)", validators=[DataRequired(), URL()])
    location = StringField("Location of Cafe", validators=[DataRequired()])
    seats = StringField("Number of seats", validators=[DataRequired()])
    has_toilet = BooleanField("Toilet available?")
    has_wifi = BooleanField("Wifi for customers?")
    has_sockets = BooleanField("Power sockets available?")
    can_take_calls = BooleanField("Can you take calls?")
    coffee_price = StringField("Price of coffee", validators=[DataRequired()])
    submit = SubmitField('Submit')
    