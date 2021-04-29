from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL


class Exercise(FlaskForm):
    """Form for adding a new exercise"""
    #Exercise name
    name = StringField('Name', validators=[DataRequired()])
    #Body part worked
    bodyPart = SelectField('Type', choices=[('Core','Arms','Back','Chest','Legs','Shoulders','Other','Full Body', 'Cardio')])
    #Type of exercise
    category = SelectField('Category', choices=[('Barbell','Dumbbell','Machine/Other','Weighted Bodyweight','Assisted Bodyweight','Reps Only','Cardio','Duration')])

class Routine(FlaskForm):
    """Form for adding a new routine"""
    #Routine Name
    name = StringField('Name', validators=[DataRequired()])
    #List of Exercises One to Many or Many to Many
    #Book & Genre exercise will help!