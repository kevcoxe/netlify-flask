from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

login_manager = LoginManager(app)

from app import models
from app import api
