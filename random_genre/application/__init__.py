
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= os.getenv('DATABASE_URI')
db = SQLAlchemy(app)
from os import getenv
#this is all done in the yaml file now with the environment variables to see
app.config['SECRET_KEY']= getenv('SECRET_KEY')
from application import routes



