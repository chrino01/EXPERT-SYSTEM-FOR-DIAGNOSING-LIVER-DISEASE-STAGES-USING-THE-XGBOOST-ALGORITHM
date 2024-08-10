from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,static_folder='static')
app.secret_key = 'dragsystem'

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://chrinoplus@localhost/chrinoplus"
# db = SQLAlchemy(app)

from app import views


