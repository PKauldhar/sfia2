from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt, login_manager
from application.models import Movies, Users
from application.forms import addMovie, RegistrationForm, LoginForm, EmailChange, updateMovie, delete_Movie
import requests





@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(email=form.email.data, password=hash_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')




@app.route('/randomMovie', methods=['GET', 'POST'])
@login_required
def randomMovie():
    currentuser=str(current_user.id)

    rg=requests.post('http://projects_random_genre_1:5000/randomGenre',currentuser)
    #   rg=requests.post('http://projects_random_genre_1:5000/randomGenre',currentuser)
    random_genre=rg.text
    #movies_genre=Movies.query.filter_by(user_id=current_user.id, genre=random_genre).all()

    rd=requests.post('http://projects_random_director_1:5000/randomDirector',currentuser)
    random_director=rd.text
    random_movies=Movies.query.filter_by(user_id=currentuser, director=random_director, genre=random_genre ).all()
    #records = session.query(Movies).filter(movie.director == 'rd').all()
    #print(filter(and_(Movies.director == random_genre, Movies.genre ==  random_director)))



    return render_template('randomMovie.html', title='randomMovie', random=random_genre, randDir=random_director, randommovies=random_movies)



@app.route('/id')
def id():
    user=current_user
    return render_template('id.html', user=user)

@app.route('/movies', methods=['GET', 'POST'])
def movies():
    if not current_user.is_authenticated:
        return redirect(url_for('home'))
    movies = Movies.query.filter_by(user_id=current_user.id).all()
    return render_template('movies.html', title='Movies', movies=movies)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = addMovie()
    if form.validate_on_submit():
        addmovie = Movies(
            title = form.title.data,
            genre = form.genre.data,
            director = form.director.data,
            rating = form.rating.data,
            author=current_user)

        db.session.add(addmovie)
        db.session.commit()
        return redirect(url_for('movies'))
    else:
        print(form.errors)
    return render_template('add.html', title='Add',posts=addMovie, form=form)


@app.route('/update', methods=['GET', 'POST'])
def update():
    form = updateMovie()

    if form.validate_on_submit():
        movie = Movies.query.filter_by(user_id=current_user.id,title=form.title.data).first()
        movie.genre=form.genre.data
        movie.director=form.director.data
        movie.rating=form.rating.data


        db.session.commit()
        return redirect(url_for('movies'))
    else:
        print(form.errors)
    return render_template('update.html', title='Update',posts=updateMovie, form=form)


@app.route('/deleteMovie', methods=['GET', 'POST'])
def deleteMovie():
    form = delete_Movie()
    if form.validate_on_submit():
        title = Movies.query.filter_by(user_id=current_user.id,title=form.title.data).first()
        db.session.delete(title)
        db.session.commit()
        return redirect(url_for('movies'))
    else:
        print(form.errors)
    return render_template('deleteMovie.html', title='Delete', form=form)





@app.route("/account", methods=['GET', 'POST'])
def account():
    form = EmailChange()
    if form.validate_on_submit():
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)


@app.route("/account/delete", methods=["GET", "POST"])
def account_delete():
    movies = Movies.query.filter_by(user_id=current_user.id).all() 
    for movie in movies:
       db.session.delete(movie)
    user_id = current_user.id
    account = Users.query.filter_by(id=user_id).first()
    logout_user()
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
