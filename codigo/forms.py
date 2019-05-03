import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from models import Antenna, Telephone, db

bp = Blueprint('forms', __name__)


# @bp.route('/query', methods=('GET', 'POST'))
# def get_antenna():
#     """Get a post and its author by id.
#
#     Checks that the id exists and optionally that the current user is
#     the author.
#
#     :param id: id of post to get
#     :param check_author: require the current user to be the author
#     :return: the post with author information
#     :raise 404: if a post with the given id doesn't exist
#     :raise 403: if the current user isn't the author
#     """
#     if request.method == 'POST':
#         mcc = request.form['mcc']
#         net = request.form['net']
#         area = request.form['area']
#         cell = request.form['cell']
#         error = None
#         antenas = Antenna.query.filter_by(mcc=mcc, net=net, area=area, cell=cell).all()
#         antena = Antenna.query.filter_by(mcc=mcc, net=net, area=area, cell=cell).first()
#
#         if antena is None:
#             error = 'Antena inexistente'
#             flash(error)
#             return render_template('base.html', lat=40.4167278, lon=-3.7033387)
#
#         return render_template('base.html', antenas=antenas, lat=antena.lat, lon=antena.lon)
@bp.route('/query', methods=('GET', 'POST'))
def get_path():
    if request.method == 'POST':
        tel_o = request.form['tel_o']
        tel_d = request.form['tel_d']
        error = None

        # falta modificar join para que contenga date_init
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

    return render_template('base.html', calls=calls)  # , lat=antenna.lat, lon=antenna.lon)
