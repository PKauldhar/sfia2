from flask import render_template, redirect, url_for, request,Response
from application import app
#db
#from application.forms import favGenre
import requests
import random

#@app.route('/helloworld')
#def get_helloworld():
 #   return {"data": "HelloWorld"}

@app.route('/randomGenre')
def get_randomMovie():
    genres_list=[]
    movies = movies.query.filter_by().all() 
    for movie in movies:
       genres_list.append(movie.genre)
       genres_list = list(dict.fromkeys(genres_list)) #removes duplicates

    random_genre = random.choice(genres_list)
    return random_genre
#	return "hi"
