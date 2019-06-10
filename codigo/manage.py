import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

# Hay que definir la variable de entorno APP_SETTINGS antes de ejecutar el código
app.config.from_object(os.environ['APP_SETTINGS'])


# Este código es para poder realizar una migración de BD desde terminal
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
