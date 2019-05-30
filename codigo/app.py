import os
from flask import Flask, render_template
from flask_migrate import Migrate
from models import db

import forms

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Aquí se configura la BD
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


@app.route('/')
def index():
    return render_template('base.html')


if __name__ == '__main__':
    app.run()
