#!/usr/bin/env python
from numpy import genfromtxt
from app import app
from models import db, Antenna


db.init_app(app)


def load_data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()


def populate():
    with app.app_context():
        try:
            file_name = "214.csv"
            data = load_data(file_name)
            for row in data:
                antenna = Antenna(radio=row[0], mcc=row[1], net=row[2], area=row[3], cell=row[4], unit=row[5],
                                  lon=row[6], lat=row[7], range=row[8], samples=row[9], changeable=row[10], created=row[11],
                                  updated=row[12], averageSignal=row[13])
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
