import os
from flask import Flask, render_template
from models import db, Antenna


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
db.init_app(app)
# with app.app_context():
#     db.create_all()
    # admin = User(username='admin', email='admin@example.com')
    # guest = User(username='guest', email='guest@example.com')
    # db.session.add(admin)
    # db.session.add(guest)
    # db.session.commit()
    # print(User.query.all())
    # print(User.query.filter_by(username='admin').first())
with app.app_context():
    antenas = Antenna.query.limit(5).all()
    for antena in antenas:
        print(antena)

@app.route('/')
def index():
    return render_template('base.html', antenas=antenas, lon=1.304765,lat=38.982559)

# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()
