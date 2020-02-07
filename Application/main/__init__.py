from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#Update with our database details to connect with database 
app.config['SECRET_KEY'] =  ""
app.config['SQLALCHEMY_DATABASE_URI'] = ""

db = SQLAlchemy(app)

from main import routes

