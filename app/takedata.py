from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TakeData(FlaskForm):
    twitter_user = StringField('Twitter user', validators=[DataRequired("Please, we need a Twitter user to analyze")])
    environment = BooleanField('Environment')
    guncontrol = BooleanField('Gun Control')
    newissue = StringField('Add issue')
    submit = SubmitField('Fit')

