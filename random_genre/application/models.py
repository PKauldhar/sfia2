
from application import db
from datetime import datetime

#Test change for jenkins


class Movies(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(30), nullable=False, unique=True)
        genre = db.Column(db.String(30), nullable=False)
        director = db.Column(db.String(30), nullable=False)
        rating = db.Column(db.String(1), nullable=False)
        date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
        user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

        def __repr__(self):
            return ''.join(["User ID: ",self.user_id,"\r\n,""Title: ", self.title,"\r\n","Genre: ", self.genre,"Director:  ",self.director,"\r\n","Rating: ",self.rating])