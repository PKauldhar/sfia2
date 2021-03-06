from flask import render_template, redirect, url_for, request,Response
from application import app, db, bcrypt, login_manager
from application.models import Movies, Users
from flask_login import login_user, current_user, logout_user, login_required
#from application.forms import favGenre
import requests
import random

#@app.route('/helloworld')
#def get_helloworld():
 #   return {"data": "HelloWorld"}

@app.route('/randomGenre', methods=['GET', 'POST'])
def get_randomMovie():
    genres_list=[]
    userid=request.data.decode("utf-8")
    user=int(userid)
    movies=Movies.query.filter_by(user_id=user).all()
    for movie in movies:
       genres_list.append(movie.genre)
       genres_list = list(dict.fromkeys(genres_list)) #removes duplicates
    
    random_genre = random.choice(genres_list)
    return random_genre
#	return "hi"