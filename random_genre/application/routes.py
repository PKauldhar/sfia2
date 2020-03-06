from flask import render_template, redirect, url_for, request,Response
from application import app, db
from application.models import Movies, Users
#from application.forms import favGenre
import requests
import random

#@app.route('/helloworld')
#def get_helloworld():
 #   return {"data": "HelloWorld"}

@app.route('/randomGenre')
def get_randomMovie():
    genres_list=[]
    movies=Movies.query.filter_by(user_id=current_user.id, genre=random_genre).all()
    for movie in movies:
       genres_list.append(movie.genre)
       genres_list = list(dict.fromkeys(genres_list)) #removes duplicates

    random_genre = random.choice(genres_list)
    print(random_genre)
    return random_genre
#	return "hi"