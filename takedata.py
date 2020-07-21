from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import validators

class TakeData(FlaskForm):
    twitter_user = StringField('Twitter user', validators=[validators.DataRequired("Please, we need a Twitter user to analyze")])
    environment = BooleanField('Environment')
    guncontrol = BooleanField('Gun Control')
    newissue = StringField('Add issue')
    submit = SubmitField('Fit')
