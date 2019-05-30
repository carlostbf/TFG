from flask_sqlalchemy import SQLAlchemy
from geoalchemy2.types import Geometry

db = SQLAlchemy()


class Antenna(db.Model):
    mcc = db.Column(db.Integer, primary_key=True, default=214)
    mnc = db.Column(db.Integer, primary_key=True)
    lac = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer, primary_key=True)

    lon = db.Column(db.Float)
    lat = db.Column(db.Float)
    range = db.Column(db.Integer)
    point = db.Column(Geometry(geometry_type="POINT"))

    # una antena puede tener varios numeros asociados
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


class Telephone(db.Model):
    tel_o = db.Column(db.BigInteger, primary_key=True)
    tel_d = db.Column(db.BigInteger, primary_key=True)

    mcc = db.Column(db.Integer, default=214)
    mnc = db.Column(db.Integer)
    lac = db.Column(db.Integer)
    cid = db.Column(db.Integer)

    date_init = db.Column(db.DateTime, primary_key=True)
    duration = db.Column(db.Integer)

    # foreign key al primary key de Antenna
    __table_args__ = (
        db.ForeignKeyConstraint(['mcc', 'mnc', 'lac', 'cid'],
                                ['antenna.mcc', 'antenna.mnc', 'antenna.lac', 'antenna.cid']),
    )
