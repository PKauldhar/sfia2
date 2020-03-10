from application import db
from application.models import Movies
import pandas as pd

#db.drop_all()
db.create_all()


data = pd.read_csv('./movies.csv')
data.columns= [0,1,2,3]

for index,row in data.iterrows():
	Movie = Movies(title=row[0], genre =row[1], director=row[2], rating=row[3],user_id=1)
	db.session.add(Movie)
db.session.commit()