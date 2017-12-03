from flask import Flask
#from flask_reggie import Reggie
app = Flask(__name__)
#Reggie(app)
from app import views
