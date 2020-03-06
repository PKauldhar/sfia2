from flask import render_template, redirect, url_for, request,Response
from application import app, db
from application.models import Movies, Users
#from application.forms import favGenre
import requests
import random

#@app.route('/helloworld')
#def get_helloworld():
 #   return {"data": "HelloWorld"}

@app.route('/randomDirector')
def get_randomDirector():
    director_list=[]
    movies=Movies.query.all()
    for movie in movies:
       director_list.append(movie.director)
       director_list = list(dict.fromkeys(director_list)) #removes duplicates

    random_director = random.choice(director_list)
    #print(random_genre)
    return random_director
#	return "hi"