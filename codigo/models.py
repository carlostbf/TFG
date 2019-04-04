from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# class BaseModel(db.Model):
#     """Base data model for all objects"""
#     __abstract__ = True
#
#     def __init__(self, *args):
#         super().__init__(*args)
#
#     def __repr__(self):
#         """Define a base way to print models"""
#         return '%s(%s)' % (self.__class__.__name__, {
#             column: value
#             for column, value in self._to_dict().items()
#         })
#
#     def json(self):
#         """
#                 Define a base way to jsonify models, dealing with datetime objects
#         """
#         return {
#             column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
#             for column, value in self._to_dict().items()
#         }


class Antenna(db.Model):
    radio = db.Column(db.String(50))
    mcc = db.Column(db.Integer, primary_key=True)
    net = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.Integer, primary_key=True)
    cell = db.Column(db.Integer, primary_key=True)
    unit = db.Column(db.Integer)
    lon = db.Column(db.Float)
    lat = db.Column(db.Float)
    range = db.Column(db.Integer)
    samples = db.Column(db.Integer)
    changeable = db.Column(db.Boolean)
    created = db.Column(db.Numeric)
    updated = db.Column(db.Numeric)
    averageSignal = db.Column(db.Integer)


class Telephone(db.Model):
    fecha_inicio = db.Column(db.DateTime, primary_key=True)
    fecha_fin = db.Column(db.DateTime)
    duracion = db.Column(db.Float)

    tlf_o = db.Column(db.Integer, primary_key=True)
    lac = db.Column(db.Integer)
    cellid = db.Column(db.Integer)
    cgi_o = db.Column(db.String(50))
    latitud_o = db.Column(db.Float)
    longitud_o = db.Column(db.Float)

    tlf_d = db.Column(db.Integer, primary_key=True)
    cgi_d = db.Column(db.String(50))
    latitud_d = db.Column(db.Float)
    longitud_d = db.Column(db.Float)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username