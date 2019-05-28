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
    """Gets the antennas to which a telephone was connected

    :param id: id of post to get
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
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

        # if call is None:
        #     error = 'Telefonos inexistente'
        #     flash(error)
        #     return render_template('base.html', lat=40.4167278, lon=-3.7033387)

        # print(len(calls))
        # for call in calls:
        #     print(call)
        #     print(call.date_init)
        #     print(call.duration)
        #     print(call.Antenna.cid)
        #     print(call.Antenna.lat)

    return render_template('base.html', calls=calls)


@bp.route('/query2', methods=('GET', 'POST'))
def get_path2():
    if request.method == 'POST':
        lat = request.form['lat']
        lon = request.form['lon']
        range = request.form['range']
        error = None

        # TODO algoritmo distancias

        pt = WKTElement('POINT({0} {1})'.format(lon, lat))
        tels = Antenna.query.join(Antenna.telephones).add_columns(Telephone.date_init, Telephone.duration,
                                                                  Telephone.tel_o, Telephone.tel_d).filter(
            func.ST_Distance_Sphere(Antenna.point, pt) < range + Antenna.range).order_by(Telephone.date_init).all()

    return render_template('base.html', tels=tels, lat=lat, lon=lon, range=range)
