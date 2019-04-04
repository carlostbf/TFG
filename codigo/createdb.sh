#!/bin/bash
#sudo -i -u postgres

sudo -u postgres psql
	ALTER USER postgres PASSWORD 'password';

sudo -u postgres createdb tfg -h localhost -p 5432

#modificar parametros postgres
export APP_SETTINGS="config.DevelopmentConfig"
python populate.py