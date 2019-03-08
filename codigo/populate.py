#!/usr/bin/env python
from io import TextIOWrapper
import csv
from numpy import genfromtxt
from app import app
from models import db, Antenna

# Create Flaskk app, config the db and load the db object
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)
db.init_app(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#
#     def __repr__(self):
#         return "<User: {}>".format(self.username)


def load_data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()


def populate():
    try:
        file_name = "214.csv"
        data = load_data(file_name)
        for row in data:
            antenna = Antenna(radio=row[0], mcc=row[1], net=row[2], area=row[3], cell=row[4], unit=row[5], lon=row[6], lat=row[7], range=row[8],
                              samples=row[9], changeable=row[10], created=row[11], updated=row[12], averageSignal=row[13])
            with app.app_context():
                db.session.add(antenna)
                db.session.commit()
    except:
        print('Error introduciendo antenas')
        db.session.rollback() #Rollback the changes on error
    return

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    populate()