from flask import render_template, redirect, url_for, request,Response
from application import app, db
from application.models import Movies, Users

import requests
import random

#@app.route('/helloworld')
#def get_helloworld():
 #   return {"data": "HelloWorld"}

@app.route('/randomDirector')
def get_randomDirector():
    director_list=[]
    movies=Movies.query.filter_by(user_id=current_user.id, genre=random_genre).all()
    for movie in movies:
       director_list.append(movie.director)
       director_list = list(dict.fromkeys(director_list)) #removes duplicates

    random_director = random.choice(director_list)

    return random_director
#	return "hi"