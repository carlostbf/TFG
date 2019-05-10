#!/bin/bash
#sudo -i -u postgres

sudo -u tfg_user psql
	ALTER USER tfg_user PASSWORD 'tfg_pw';

sudo -u tfg_user createdb tfg -h localhost -p 5434

#modificar parametros postgres
. venv/bin/activate
export APP_SETTINGS="config.DevelopmentConfig"
python populate.py