from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    # TODO: Add the following fields to the form class:
    # - title - StringField
    title = StringField('title', validators=[DataRequired()])
    # - address - StringField
    address = StringField('address', validators=[DataRequired()])
    # - submit button
    submit = InlineButton('submit')

class GroceryItemForm(FlaskForm):
    # TODO: Add the following fields to the form class:
    """Form for adding/updating a GroceryItem."""
    # - name - StringField
    name = StringField('name', validators=[DataRequired()])
    # - price - FloatField
    price = FloatField('price', validators=[DataRequired()])
    # - category - SelectField (specify the 'choices' param)
    category = SelectField('category', choices =[('Bananas','Strawberries','Yogurt')])
    # - photo_url - StringField (use a URL validator)
    photo_url = StringField('photo_url', validators=[URL(required_tld=True, message=None)])
    # - store - QuerySelectField (specify the `query_factory` param)
    store = QuerySelectField('store')
    # - submit button
    submit = SubmitField('Submit!')


class SignUpForm(FlaskForm):
    ''' Form for adding a User '''
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    ''' Form for logging in a User '''
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
