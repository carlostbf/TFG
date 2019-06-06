from datetime import *

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from models import Antenna, Telephone, db
from sqlalchemy import func, or_, tuple_
from sqlalchemy.orm import aliased
from geoalchemy2.elements import WKTElement

bp = Blueprint('forms', __name__)


@bp.route('/query', methods=('GET', 'POST'))
def get_path():
    """Dado un teléfono y 2 instantes de tiempo, obtiene las antenas a las
    que se ha conectado.

    :param tel: teléfono objetivo
    :param date_init: fecha a partir de la que se filtra
    :param date_end: fecha hasta la que se filtra

    :return: calls: Contiene todos los datos de antenas y del teléfono objetivo
    """
    # if request.method == 'POST':
    tel = request.form['tel']
    date_init = request.form['date_init']
    date_end = request.form['date_end']
    error = None

    if date_init == '':
        date_init = datetime.min
    if date_end == '':
        date_end = datetime.max

    calls = Antenna.query.join(Antenna.telephones).add_columns(Telephone.date_init, Telephone.duration,
                                                               Telephone.tel_o, Telephone.tel_d).filter(
        date_init <= Telephone.date_init, Telephone.date_init <= date_end).filter(
        or_(Telephone.tel_o == tel, Telephone.tel_d == tel)).order_by(Telephone.date_init).all()

    # VER TELÉFONOS QUE HAN REALIZADO LLAMADAS CASI AL MISMO TIEMPO QUE OBJETIVO EN MISMO LUGAR
    return render_template('base.html', calls=calls, tel=tel, date_init=date_init, date_end=date_end)


@bp.route('/query2', methods=('GET', 'POST'))
def get_path2():
    """Dadas una latitud y longitud, un rango de búsqueda y 2 instantes de tiempo, obtiene
    los teléfonos que se conectaron a antenas en esa ubicación con ese rango y entre los instantes de tiempo fijados.

    :param lat: coordenada de latitud
    :param lon: coordenada de longitud
    :param radio: radio de búsqueda alrededor de (lat,lon)
    :param date_init: fecha a partir de la que se filtra
    :param date_end: fecha hasta la que se filtra

    :return: tels: Contiene todos los datos de antenas y teléfonos del filtro.
    """
    # if request.method == 'POST':
    lat = request.form['lat']
    lon = request.form['lon']
    radio = request.form['range']
    date_init = request.form['date_init']
    date_end = request.form['date_end']
    slider = int(request.form['slider'])
    print(slider)
    error = None

    if date_init == '':
        date_init = datetime.min
    if date_end == '':
        date_end = datetime.max

    pt = WKTElement('POINT({0} {1})'.format(lon, lat))
    # Consulta para encontrar llamadas en la ubicación (sin filtros de tiempo de estancia)
    stmt1 = Antenna.query.join(Antenna.telephones).add_columns(Telephone.date_init, Telephone.duration,
                                                               Telephone.tel_o, Telephone.tel_d).filter(
        date_init <= Telephone.date_init, Telephone.date_init <= date_end).filter(
        func.ST_Distance_Sphere(Antenna.point, pt) < radio + Antenna.range).order_by(Telephone.date_init)
    # tels = stmt1.all()

    telephone_alias = aliased(Telephone)
    antenna_alias = aliased(Antenna)
    dif = (func.max(telephone_alias.date_init) - func.min(telephone_alias.date_init)).label("dif")
    # Consulta para encontrar todos los teléfonos que cumplen estancia superior a X minutos
    # en una ubicación en el periodo fijado
    stmt2 = db.session.query(telephone_alias.tel_o, antenna_alias.lon, antenna_alias.lat).join(
        telephone_alias, antenna_alias.telephones).filter(
        date_init <= telephone_alias.date_init, telephone_alias.date_init <= date_end).group_by(
        telephone_alias.tel_o, antenna_alias.lon,
        antenna_alias.lat).having(
        dif >= timedelta(minutes=slider))

    # VER TELÉFONOS QUE SE HAN QUEDADO QUIETOS EN EL LUGAR
    # coger tels con mismo tel_o y ver si ha hecho llamadas con distancia en tiempo de más de X mins
    tels = stmt1.filter(tuple_(Telephone.tel_o, Antenna.lon, Antenna.lat).in_(stmt2)).all()
    # print(stmt1)
    # print(len(stmt1.all()))
    # print(stmt2)
    # print(len(stmt2.all()))
    #
    # print(len(tels))

    return render_template('base.html', tels=tels, lat=lat, lon=lon, radio=radio, date_init=date_init,
                           date_end=date_end, slider=slider)
