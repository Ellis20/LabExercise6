import os
from flask import render_template, url_for, request, redirect, flash, session
from main import app, db
#Use to import data models to use data
#e.g from main.models import Tweets...
#from shop.models import Products, User

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
        return render_template('home.html')

