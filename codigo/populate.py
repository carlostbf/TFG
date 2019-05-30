#!/usr/bin/env python
import sys
import json
import pandas as pd
from app import app
from models import db, Antenna, Telephone

db.init_app(app)


def load_tel(file_name, imodel):
    with open("models.json", "r") as read_file:
        data = json.load(read_file)

    model = data['calls'][imodel]

    # leemos sólo las columnas necesarias
    cols = [
        model['tel_o'],
        model['tel_d'],

        model['mcc'],
        model['mnc'],
        model['lac'],
        model['cid'],

        model['date_init'],
        model['duration']
    ]
    df = pd.read_excel(file_name, usecols=cols)

    # unificamos los nombres de las columnas
    df.rename(columns={
        model['tel_o']: 'tel_o',
        model['tel_d']: 'tel_d',

        model['mcc']: 'mcc',
        model['mnc']: 'mnc',
        model['lac']: 'lac',
        model['cid']: 'cid',

        model['date_init']: 'date_init',
        model['duration']: 'duration'
    }, inplace=True)

    # comprobamos telefonos repetidas para no insertarlas
    records = df.to_dict(orient="records")
    print("TELEFONOS REPETIDOS")
    for rec in list(records):
        # tel = Telephone.query.get({"tel_o": rec['tel_o'], "tel_d": rec['tel_d'], "date_init": rec['date_init']})
        tel = Telephone.query.get((rec['tel_o'], rec['tel_d'], rec['date_init']))
        if tel is not None:
            print(tel)
            records.remove(rec)
    with app.app_context():
        db.session.bulk_insert_mappings(Telephone, records)
        db.session.commit()

    return


def load_ant(file_name, imodel):
    with open("models.json", "r") as read_file:
        data = json.load(read_file)

    model = data['antennas'][imodel]

    # leemos sólo las columnas necesarias
    cols = [
        model['mcc'],
        model['mnc'],
        model['lac'],
        model['cid'],

        model['lon'],
        model['lat'],
        model['range']
    ]
    df = pd.read_excel(file_name, usecols=cols)

    # unificamos los nombres de las columnas
    df.rename(columns={
        model['mcc']: 'mcc',
        model['mnc']: 'mnc',
        model['lac']: 'lac',
        model['cid']: 'cid',

        model['lon']: "lon",
        model['lat']: "lat",
        model['range']: "range"
    }, inplace=True)
    # comprobamos antenas repetidas para no insertarlas
    records = df.to_dict(orient="records")
    print("ANTENAS REPETIDAS")
    for rec in list(records):
        ant = Antenna.query.get((rec['mcc'], rec['mnc'], rec['lac'], rec['cid']))
        if ant is not None:
            print(ant)
            records.remove(rec)
    with app.app_context():
        db.session.bulk_insert_mappings(Antenna, records)
        db.session.commit()
        Antenna.update_geometries()

    return


if __name__ == '__main__':
    file_name = "llamadas.xlsx"
    with app.app_context():
        # db.drop_all()
        db.create_all()
        load_ant("antenas.xlsx", 1)
        load_tel("llamadas.xlsx", 0)
