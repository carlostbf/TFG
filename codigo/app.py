import os
from flask import Flask, render_template
from flask_migrate import Migrate
from models import db, Antenna, Point

import forms
from geoalchemy2.elements import WKTElement

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

POSTGRES = {
    'user': 'tfg_user',
    'pw': 'tfg_pw',
    'db': 'tfg',
    'host': 'localhost',
    'port': '5434',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

app.register_blueprint(forms.bp)
db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()
    # antenas = Antenna.query.limit(2).all()
    # first = Antenna.query.first()
    # for antena in antenas:
    #     print(antena)


def get_nearest(lat, lon):
    # find the nearest point to the input coordinates
    # convert the input coordinates to a WKT point and query for nearest point
    pt = WKTElement('POINT({0} {1})'.format(lon, lat), srid=4326)
    return Point.query.order_by(Point.geom.distance_box(pt)).first()


@app.route('/')
def index():
    # return render_template('base.html', antenas=antenas, lat=40.4167278, lon=-3.7033387)
    return render_template('base.html')


if __name__ == '__main__':
    app.run()
