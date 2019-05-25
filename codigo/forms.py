import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from models import Antenna, Telephone
from geopy.distance import geodesic

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
        tel_o = request.form['tel_o']
        tel_d = request.form['tel_d']
        error = None

        # TODO falta modificar join para que contenga date_init
        calls = Antenna.query.join(Antenna.telephones).add_columns(Telephone.date_init, Telephone.duration).filter_by(
            tel_o=tel_o, tel_d=tel_d).order_by(Telephone.date_init).all()

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
        # print(Point.query.filter(func.ST_Distance_Sphere(Point.geom, Point.query.first().geom) < 100000000000000).all())

        Antenna.query.join(Antenna.telephones).filter().order_by(Telephone.date_init).all()
        #Antenna.query.join(Antenna.telephones).filter_by().order_by(Telephone.date_init).all()


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


def distance(lon1, lat1, lon2, lat2):
    point1 = (lat1, lon1)
    point2 = (lat2, lon2)
    return geodesic(point1, point2).m
