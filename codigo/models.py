from flask_sqlalchemy import SQLAlchemy
from geoalchemy2.types import Geometry

db = SQLAlchemy()


# Clase para almacenar las antenas
class Antenna(db.Model):
    # Id de las antenas
    mcc = db.Column(db.Integer, primary_key=True, default=214)
    mnc = db.Column(db.Integer, primary_key=True)
    lac = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer, primary_key=True)

    # Coordenadas en latitud y longitud
    lon = db.Column(db.Float)
    lat = db.Column(db.Float)

    # Radio de alcance de las antenas
    range = db.Column(db.Integer)

    # Objeto donde se almacena la latitud y longitud para posteriores consultas con PostGIS
    point = db.Column(Geometry(geometry_type="POINT"))

    # una antena puede tener varios numeros que han llamado usando dicha antena
    telephones = db.relationship('Telephone', lazy=True, backref='antenna')

    def __repr__(self):
        return "<antenna {mcc} {mnc} {lac} {cid} ({lat}, {lon})>".format(
            mcc=self.mcc, mnc=self.mnc, lac=self.lac, cid=self.cid, lat=self.lat, lon=self.lon)

    @classmethod
    def update_geometries(cls):
        """Esta función rellena la columna point con los datos proporcionados
            por la latitud y longitud una vez han sido rellenados"""

        ants = Antenna.query.all()

        for ant in ants:
            point = 'POINT({} {})'.format(ant.lon, ant.lat)
            ant.point = point

        db.session.commit()


# Clase para almacenar los registros de llamada telefónicos
class Telephone(db.Model):
    # Teléfono origen de llamada
    tel_o = db.Column(db.BigInteger, primary_key=True)
    # Teléfono destino de llamada
    tel_d = db.Column(db.BigInteger, primary_key=True)

    # id de la antena a la que se conecta
    mcc = db.Column(db.Integer, default=214)
    mnc = db.Column(db.Integer)
    lac = db.Column(db.Integer)
    cid = db.Column(db.Integer)

    # Fecha de inicio de llamada
    date_init = db.Column(db.DateTime, primary_key=True)
    # Duración en segundos de llamada
    duration = db.Column(db.Integer)

    # Foreign key al primary key de Antenna
    __table_args__ = (
        db.ForeignKeyConstraint(['mcc', 'mnc', 'lac', 'cid'],
                                ['antenna.mcc', 'antenna.mnc', 'antenna.lac', 'antenna.cid']),
    )

    def __repr__(self):
        return "<telephone {tel_o} {tel_d} {date_init}>".format(
            tel_o=self.tel_o, tel_d=self.tel_d, date_init=self.date_init)
