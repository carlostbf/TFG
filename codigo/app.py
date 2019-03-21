import os
from flask import Flask, render_template
from models import db, Antenna
import forms

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'tfg',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

app.register_blueprint(forms.bp)
db.init_app(app)

with app.app_context():
    antenas = Antenna.query.limit(2).all()
    first = Antenna.query.first()
    for antena in antenas:
        print(antena)


@app.route('/')
def index():
    return render_template('base.html', antenas=antenas, lat=40.4167278, lon=-3.7033387)


if __name__ == '__main__':
    app.run()
