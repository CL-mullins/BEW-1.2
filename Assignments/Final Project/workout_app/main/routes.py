from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from workout_app.models import Exercise, Routine
from workout_app import bcrypt

from workout_app import app, db

main = Blueprint("main", __name__)

##########################################
#               Routes                  #
#########################################

@main.route('/')
def homepage():
    #TODO: Create homepage
    return render_template('homepage.html')

@main.route('/add_exercise', methods=['GET', 'POST'])
@login_required
def add_exercise():
    form = ExerciseForm()

    if form.validate_on_submit():
        new_exercise = Exercise

    pass