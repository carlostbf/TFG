import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from models import Antenna

bp = Blueprint('forms', __name__)



@bp.route('/query', methods=('GET', 'POST'))
def get_antenna():
    """Get a post and its author by id.

    Checks that the id exists and optionally that the current user is
    the author.

    :param id: id of post to get
    :param check_author: require the current user to be the author
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    if request.method == 'POST':
        mcc = request.form['mcc']
        net = request.form['net']
        area = request.form['area']
        cell = request.form['cell']
        error = None
        antenas = Antenna.query.filter_by(mcc=mcc, net=net, area=area, cell=cell).all()
        antena = Antenna.query.filter_by(mcc=mcc, net=net, area=area, cell=cell).first()

        if antena is None:
            error= 'Antena inexistente'
            flash(error)
            return render_template('base.html', lat=40.4167278, lon=-3.7033387)

        return render_template('base.html', antenas=antenas,lat=antena.lat,lon=antena.lon)
