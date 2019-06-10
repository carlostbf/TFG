#!/usr/bin/env python
import json
import pandas as pd
from app import app
from models import db, Antenna, Telephone

db.init_app(app)


def load_tel(data_file, model_file, imodel):
    """Dadas un nombre de fichero de llamadas telefónicas y un índice imodel del fichero de modelos model_file,
    Inserta los datos del fichero en la base de datos

    :param data_file: nombre del fichero xlsx de teléfonos a leer
    :param model_file: nombre del fichero json de modelos a leer
    :param imodel: índice de la lista de modelos

    """
    with open(model_file, "r") as read_file:
        data = json.load(read_file)

    model = data['calls'][imodel]

    # leemos sólo las columnas que aparecen en el mapeo
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
    df = pd.read_excel(data_file, usecols=cols)

    # renombramos las columnas del modelo de datos para que sea siempre el mismo
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

    # comprobamos filas repetidas para no insertarlas
    records = df.to_dict(orient="records")
    print("LISTA DE TELEFONOS REPETIDOS:")
    for rec in list(records):
        tel = Telephone.query.get((rec['tel_o'], rec['tel_d'], rec['date_init']))
        # Si ya está en la BD, lo imprimimos por pantalla y lo quitamos del diccionario
        if tel is not None:
            print(tel)
            records.remove(rec)

    # Insertamos sólo las filas no repetidas
    with app.app_context():
        db.session.bulk_insert_mappings(Telephone, records)
        db.session.commit()

    return


def load_ant(data_file, model_file, imodel):
    """Dadas un nombre de fichero de antenas y un índice imodel del fichero de modelos model_file,
    Inserta los datos del fichero en la base de datos

    :param data_file: nombre del fichero xlsx de antenas a leer
    :param model_file: nombre del fichero json de modelos a leer
    :param imodel: índice de la lista de modelos

    """
    with open(model_file, "r") as read_file:
        data = json.load(read_file)

    model = data['antennas'][imodel]

    # leemos sólo las columnas que aparecen en el mapeo
    cols = [
        model['mcc'],
        model['mnc'],
        model['lac'],
        model['cid'],

        model['lon'],
        model['lat'],
        model['range']
    ]
    df = pd.read_excel(data_file, usecols=cols)

    # renombramos las columnas del modelo de datos para que sea siempre el mismo
    df.rename(columns={
        model['mcc']: 'mcc',
        model['mnc']: 'mnc',
        model['lac']: 'lac',
        model['cid']: 'cid',

        model['lon']: "lon",
        model['lat']: "lat",
        model['range']: "range"
    }, inplace=True)

    # comprobamos filas repetidas para no insertarlas
    records = df.to_dict(orient="records")
    print("LISTA DE ANTENAS REPETIDAS:")
    for rec in list(records):
        ant = Antenna.query.get((rec['mcc'], rec['mnc'], rec['lac'], rec['cid']))
        # Si ya está en la BD, lo imprimimos por pantalla y lo quitamos del diccionario
        if ant is not None:
            print(ant)
            records.remove(rec)

    # Insertamos sólo las filas no repetidas
    with app.app_context():
        db.session.bulk_insert_mappings(Antenna, records)
        db.session.commit()
        # Rellena la columna de Point para las nuevas antenas
        Antenna.update_geometries()

    return


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        load_ant("antenas.xlsx", "models.json", 0)
        load_tel("llamadas.xlsx", "models.json", 0)
