from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
#app.config.from_object(Config)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)