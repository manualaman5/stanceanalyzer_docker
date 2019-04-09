from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TakeExamples(FlaskForm):
    #Retrieve users
    #dict of issues T/F
    issues = list()
    for example in example_accoutns:
        issue = BooleanField(example.name)
        issues.update({example.name : issue})

    submit = SubmitField('Fit')

