import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from models import Antenna, Telephone
from sqlalchemy import func, or_
from geoalchemy2.elements import WKTElement

bp = Blueprint('forms', __name__)


@bp.route('/query', methods=('GET', 'POST'))
def get_path():  # TODO arreglar comentarios
    """Dado un teléfono y 2 instantes de tiempo, obtiene las antenas a las
    que se ha conectado.

    :param tel: teléfono objetivo
    :param date_init: fecha a partir de la que se filtra
    :param date_end: fecha hasta la que se filtra

    :return: calls: Contiene todos los datos de antenas y del teléfono objetivo
    """
    if request.method == 'POST':
        tel = request.form['tel']
        date_init = request.form['date_init']
        date_end = request.form['date_end']
        error = None

        if date_init == '':
            date_init = datetime.datetime.min
        if date_end == '':
            date_end = datetime.datetime.max

        calls = Antenna.query.join(Antenna.telephones).add_columns(Telephone.date_init, Telephone.duration,
                                                                   Telephone.tel_o, Telephone.tel_d).filter(
            date_init <= Telephone.date_init, Telephone.date_init <= date_end).filter(
            or_(Telephone.tel_o == tel, Telephone.tel_d == tel)).order_by(Telephone.date_init).all()

    return render_template('base.html', calls=calls)


@bp.route('/query2', methods=('GET', 'POST'))
def get_path2():
    """Dadas una latitud y longitud, un rango de búsqueda y 2 instantes de tiempo, obtiene
    los teléfonos que se conectaron a antenas en esa ubicación con ese rango y entre los instantes de tiempo fijados.

    :param lat: coordenada de latitud
    :param lon: coordenada de longitud
    :param range: radio de búsqueda alrededor de (lat,lon)
    :param date_init: fecha a partir de la que se filtra
    :param date_end: fecha hasta la que se filtra

    :return: tels: Contiene todos los datos de antenas y teléfonos del filtro.
    """
    if request.method == 'POST':
        lat = request.form['lat']
        lon = request.form['lon']
        range = request.form['range']
        date_init = request.form['date_init']
        date_end = request.form['date_end']
        error = None

        if date_init == '':
            date_init = datetime.datetime.min
        if date_end == '':
            date_end = datetime.datetime.max

        pt = WKTElement('POINT({0} {1})'.format(lon, lat))
        tels = Antenna.query.join(Antenna.telephones).add_columns(Telephone.date_init, Telephone.duration,
                                                                  Telephone.tel_o, Telephone.tel_d).filter(
            date_init <= Telephone.date_init, Telephone.date_init <= date_end).filter(
            func.ST_Distance_Sphere(Antenna.point, pt) < range + Antenna.range).order_by(Telephone.date_init).all()

    return render_template('base.html', tels=tels, lat=lat, lon=lon, range=range)
