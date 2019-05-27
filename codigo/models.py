from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2.types import Geometry
from sqlalchemy import func

db = SQLAlchemy()


# una antena puede tener varios numeros asociados
class Antenna(db.Model):
    mcc = db.Column(db.Integer, primary_key=True, default=214)
    mnc = db.Column(db.Integer, primary_key=True)
    lac = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer, primary_key=True)

    lon = db.Column(db.Float)
    lat = db.Column(db.Float)
    range = db.Column(db.Integer)
    point = db.Column(Geometry(geometry_type="POINT"))

    telephones = db.relationship('Telephone', lazy=True, backref='antenna')

    def __repr__(self):
        return "<antenna {cid} ({lat}, {lon})>".format(
            cid=self.cid, lat=self.lat, lon=self.lon)

    @classmethod
    def update_geometries(cls):
        """Using each city's longitude and latitude, add geometry data to db."""

        ants = Antenna.query.all()

        for ant in ants:
            point = 'POINT({} {})'.format(ant.lon, ant.lat)
            ant.point = point

        db.session.commit()



class Telephone(db.Model):
    tel_o = db.Column(db.BigInteger, primary_key=True)
    tel_d = db.Column(db.BigInteger, primary_key=True)

    # foreign key a antena
    mcc = db.Column(db.Integer, default=214)
    mnc = db.Column(db.Integer)
    lac = db.Column(db.Integer)
    cid = db.Column(db.Integer)

    date_init = db.Column(db.DateTime, primary_key=True)
    duration = db.Column(db.Integer)

    __table_args__ = (
        db.ForeignKeyConstraint(['mcc', 'mnc', 'lac', 'cid'],
                                ['antenna.mcc', 'antenna.mnc', 'antenna.lac', 'antenna.cid']),
    )
