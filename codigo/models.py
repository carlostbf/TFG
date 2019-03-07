from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


# class Antena(BaseModel, db.Model):
#     __tablename__='antenas'
#
#     radio=db.Column(db.Integer)
#     mcc=db.Column(db.Integer)
#     net=db.Column(db.Integer)
#     area=db.Column(db.Integer)
#     cell=db.Column(db.Integer)
#     unit=db.Column(db.Integer)
#     lon=db.Column(db.Float)
#     lat=db.Column(db.Float)
#     range=db.Column(db.Integer)
#     samples=db.Column(db.Integer)
#     changeable=db.Column(db.Boolean)
#     created=db.Column(db.DateTime)
#     updated=db.Column(db.DateTime)
#     averageSignal=db.Column(db.Integer)

    #db.Relationship



class Station(BaseModel, db.Model):
    """Model for the stations table"""
    __tablename__ = 'stations'

    id = db.Column(db.Integer, primary_key = True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)