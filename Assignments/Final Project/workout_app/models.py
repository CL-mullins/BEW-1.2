from sqlalchemy_utils import URLType

class Exercise(db.Model):
    """Exercise Model"""
    #Import data from Exercise Form as to which category & body part worked
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    #If I want pounds and reps to be contingent on the type of category, make nullable set to true.
    #I want to hide certain form fields (FrontEnd work)
    #If i want to reject information on back end i could use a validator to reject form based on category.
    pounds = db.Column(db.Float, nullable=True)
    reps = db.Column(db.Integer, nullable=True)