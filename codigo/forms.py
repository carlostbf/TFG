from datetime import *

from flask import (
    Blueprint, render_template, request
)

from models import Antenna, Telephone, db
from sqlalchemy import func, tuple_
from sqlalchemy.orm import aliased
from geoalchemy2.elements import WKTElement

bp = Blueprint('forms', __name__)


@bp.route('/query', methods=('GET', 'POST'))
def get_path():
    """Dado un teléfono y 2 instantes de tiempo, obtiene las antenas a las
    que se ha conectado (si se marca el checkbox, muestra también el resto de teléfonos).

    :param tel: teléfono objetivo
    :param date_init: fecha a partir de la que se filtra
    :param date_end: fecha hasta la que se filtra
    :oaram resto: checkbox para decidir si mostrar también el resto de teléfonos en la misma zona

    :return: calls: Contiene todos los datos de antenas y del filtro
    """
    tel = request.form['tel']
    date_init = request.form['date_init']
    date_end = request.form['date_end']
    resto = request.form.get('resto')
    error = None

    # En caso de que no se defina las fechas
    if date_init == '':
        date_init = datetime.min
    if date_end == '':
        date_end = datetime.max

    # defino alias para las consultas
    telephone_alias = aliased(Telephone)
    antenna_alias = aliased(Antenna)

    # llamadas realizadas por tel entre date_init y date_end ordenados por date_init
    stmt1 = Antenna.query.join(Antenna.telephones). \
        add_columns(Telephone.date_init, Telephone.duration, Telephone.tel_o, Telephone.tel_d). \
        filter(date_init <= Telephone.date_init, Telephone.date_init <= date_end). \
        filter(Telephone.tel_o == tel). \
        order_by(Telephone.date_init)

    # como stmt1, pero con todos los teléfonos distintos de tel
    stmt2 = Antenna.query.join(Antenna.telephones). \
        add_columns(Telephone.date_init, Telephone.duration, Telephone.tel_o, Telephone.tel_d). \
        filter(date_init <= Telephone.date_init, Telephone.date_init <= date_end). \
        filter(Telephone.tel_o != tel)

    # todas las coordenadas distintas donde ha llamado tel
    stmt3 = db.session.query(antenna_alias.lon, antenna_alias.lat).distinct(). \
        join(telephone_alias, antenna_alias.telephones). \
        filter(date_init <= telephone_alias.date_init, telephone_alias.date_init <= date_end). \
        filter(telephone_alias.tel_o == tel)

    # telefonos distintos de tel, que estan en las mismas coordenadas que tel
    stmt4 = stmt2.filter(tuple_(Antenna.lon, Antenna.lat).in_(stmt3))
    # En caso de que se quieran mostrar también los otros teléfonos distintos de tel en su misma zona
    if resto:
        calls = stmt1.union(stmt4).order_by(Telephone.date_init).all()
    # En caso de que solo se quiera mostrar a tel
    else:
        calls = stmt1.all()

    return render_template('base.html', calls=calls, tel=tel, date_init=date_init, date_end=date_end, resto=resto)


@bp.route('/query2', methods=('GET', 'POST'))
def get_path2():
    """Dadas una latitud y longitud, un rango de búsqueda y 2 instantes de tiempo, obtiene
    los teléfonos que se conectaron a antenas en esa ubicación con ese rango y entre los instantes de tiempo fijados.
    El valor de slider, es el tiempo mínimo de estancia de un teléfono para que aparezca en el filtro.

    :param lat: coordenada de latitud
    :param lon: coordenada de longitud
    :param radio: radio de búsqueda alrededor de (lat,lon)
    :param date_init: fecha a partir de la que se filtra
    :param date_end: fecha hasta la que se filtra
    :param slider: tiempo de estancia mínimo que debe haber estado un teléfono para que aparezca

    :return: tels: Contiene todos los datos de antenas y teléfonos del filtro.
    """
    lat = request.form['lat']
    lon = request.form['lon']
    radio = request.form['range']
    date_init = request.form['date_init']
    date_end = request.form['date_end']
    slider = int(request.form['slider'])
    error = None

    # En caso de que no se defina las fechas
    if date_init == '':
        date_init = datetime.min
    if date_end == '':
        date_end = datetime.max

    # Punto en coordenadas para aplicar el filtro
    pt = WKTElement('POINT({0} {1})'.format(lon, lat))

    # Consulta para encontrar llamadas en la ubicación en el periodo fijado (sin filtros de tiempo de estancia)
    stmt1 = Antenna.query.join(Antenna.telephones). \
        add_columns(Telephone.date_init, Telephone.duration, Telephone.tel_o, Telephone.tel_d). \
        filter(date_init <= Telephone.date_init, Telephone.date_init <= date_end). \
        filter(func.ST_Distance_Sphere(Antenna.point, pt) < radio + Antenna.range). \
        order_by(Telephone.date_init)

    # alias definidos para la consulta
    telephone_alias = aliased(Telephone)
    antenna_alias = aliased(Antenna)

    # alias para la distancia máxima entre las 2 llamadas de un mismo teléfono
    dif = (func.max(telephone_alias.date_init) - func.min(telephone_alias.date_init)).label("dif")

    # Consulta para encontrar todos los teléfonos (por ubicacion) que cumplen estancia superior a X minutos
    # en una ubicación en el periodo fijado
    stmt2 = db.session.query(telephone_alias.tel_o, antenna_alias.lon, antenna_alias.lat). \
        join(telephone_alias, antenna_alias.telephones). \
        filter(date_init <= telephone_alias.date_init, telephone_alias.date_init <= date_end). \
        group_by(telephone_alias.tel_o, antenna_alias.lon, antenna_alias.lat). \
        having(dif >= timedelta(minutes=slider))

    # coger teléfonos de stmt1 y coger los que estén también en la consulta stmt2
    tels = stmt1.filter(tuple_(Telephone.tel_o, Antenna.lon, Antenna.lat).in_(stmt2)).all()

    return render_template('base.html', tels=tels, lat=lat, lon=lon, radio=radio, date_init=date_init,
                           date_end=date_end, slider=slider)
