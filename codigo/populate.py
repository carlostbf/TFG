#!/usr/bin/env python
import json
import pandas as pd
from numpy import genfromtxt
from app import app
from models import db, Antenna, Telephone

db.init_app(app)


def load_data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()


def populate(file_name):
    with app.app_context():
        try:
            data = load_data(file_name)
            for row in data:
                antenna = Antenna(radio=row[0], mcc=row[1], net=row[2], area=row[3], cell=row[4], unit=row[5],
                                  lon=row[6], lat=row[7], range=row[8], samples=row[9], changeable=row[10],
                                  created=row[11],
                                  updated=row[12], averageSignal=row[13])
                db.session.add(antenna)

            db.session.commit()

        except:
            print('Error introduciendo antenas')
            db.session.rollback()  # Rollback the changes on error

    return


def load(csv_file, imodel):
    with open("models.json", "r") as read_file:
        data = json.load(read_file)

    # for model in data['models']:
    #     print(model)
    #     print(data['models'][0])  # model
    model = data['models'][imodel]
    #optimizable?
    df = pd.read_csv(csv_file).loc[:, [model['fecha_inicio'],
                                       model['fecha_fin'],
                                       model['duracion'],

                                       model['tlf_o'],
                                       model['cgi_o'],
                                       model['latitud_o'],
                                       model['longitud_o'],

                                       model['tlf_d'],
                                       model['cgi_d'],
                                       model['latitud_d'],
                                       model['longitud_d']
                                       ]
         ]

    # print(df.head())
    #optimizable?
    df.rename(columns={
        model['fecha_inicio']: 'fecha_inicio',
        model['fecha_fin']: 'fecha_fin',
        model['duracion']: 'duracion',

        model['tlf_o']: 'tlf_o',
        model['cgi_o']: 'cgi_o',
        model['latitud_o']: 'latitud_o',
        model['longitud_o']: 'longitud_o',

        model['tlf_d']: 'tlf_d',
        model['cgi_d']: 'cgi_d',
        model['latitud_d']: 'latitud_d',
        model['longitud_d']: 'longitud_d',

    },
        inplace=True)
    # print(df.to_dict(orient="records"))
    with app.app_context():
        db.session.bulk_insert_mappings(Telephone, df.to_dict(orient="records"))
        db.session.commit()


if __name__ == '__main__':
    file_name = "modelo_MOVISTAR.csv"
    with app.app_context():
        # db.drop_all()
        db.create_all()
    # populate(file_name="215.csv")
    load(file_name, 0)
