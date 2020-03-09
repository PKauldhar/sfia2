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

@app.route('/randomMaster', methods=['GET', 'POST'])
def get_randomMaster():
    current_user=request.data.decode("utf-8")
    #print(current_user)
    #print(str(request.data.decode("utf-8")))]#




    #currentuser=str(current_user.id)
    rg=requests.post('http://projects_random_genre_1:5000/randomGenre',current_user)
    #   rg=requests.post('http://projects_random_genre_1:5000/randomGenre',currentuser)
    random_genre=rg.text
    #movies_genre=Movies.query.filter_by(user_id=current_user.id, genre=random_genre).all()

    rd=requests.post('http://projects_random_director_1:5000/randomDirector',current_user)
    random_director=rd.text
    #random_movies=Movies.query.filter_by(user_id=current_user, director=random_director, genre=random_genre ).all()
    randomised = {'genre': random_genre, 'director': random_director}
    return (randomised)
    #records = session.query(Movies).filter(movie.director == 'rd').all()
    #print(filter(and_(Movies.director == random_genre, Movies.genre ==  random_director)))
#	return "hi"