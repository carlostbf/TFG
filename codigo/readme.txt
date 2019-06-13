ESTRUCTURA DEL CÓDIGO
codigo
    static
        css
            style.css -> el css de la interfaz
    templates
        base.html -> la interfaz gráfica, tiene todo el html y javascript
    app.py -> programa principal, se ejecuta para iniciar el servidor
    config.py -> tiene definidos los APP_SETTINGS
    forms.py -> Interpreta las requests del html, las procesa en BBDD y devuelve respuestas al html
                Tiene el código sqlalchemy
    manage.py -> se define para poder migrar los modelos de BBDD si cambian
    models.py -> contiene los modelos de BBDD
    populate.py -> contiene el script para poblar la BBDD usando los .xlsx y .json

    antenas.xlsx -> fichero con datos de antenas
    llamadas.xlsx -> fichero con datos de llamadas telefónicas
    models.json -> fichero con formatos de los ficheros de datos

    postgis.sql -> codigo sql a ejecutar para crear las estructuras que permiten usar PostGIS
    requirements.txt -> contiene las versiones de librerías usadas




MANUAL DE INSTALACION Y SETUP
    -Instalar Python 3.7.2

    -Instalar con pip las librerías en "requirements.txt"

    -BBDD (PostgreSQL 11.2)
        +Primero hay que crearse una BD con los valores:
        usuario, contraseña, nombre_BD, host, puerto
        Y rellenar los campos con estos valores en el fragmento de código que encontramos en app.py :

                    POSTGRES = {
                        'user': usuario,
                        'pw': contraseña,
                        'db': nombre_BD,
                        'host': host,
                        'port': puerto,
                    }

        +Para poder utilizar las consultas de PostGIS:
            ejecutar en SQL las consultas en "postgis.sql" para crear las estructuras necesarias en BD

    -Google Maps
        En el fichero base.html (al final del fichero), rellenar la variable YOUR_API_KEY con una clave válida en este código:
          <script async defer src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap"
          type="text/javascript"></script>


    -Ejecución de app (2 opciones):
        +Si se tiene PyCharm:
            abrir el proyecto "codigo" y ejecutar la aplicación

        +Desde terminal en la carpeta "codigo" (comandos):
            . venv/bin/activate
            export APP_SETTINGS="config.DevelopmentConfig"
            flask run

    -Popular BD (comando):

        python populate.py

        EXTRA: si se desea usar otros ficheros de datos, entrar en el script y al final del fichero alterar los parámetros en el código:

                            load_ant(antena_file, model_file, i_model)
                            load_tel(llamadas_file, model_file, i_model2)

             antena_file (nombre del fichero excel donde se guardan datos de antenas)
             llamadas_file (nombre del fichero excel donde se guardan datos de llamadas)
             model_file (fichero JSON donde se guardan los formatos de los ficheros anteriores, véase "models.json")
             i_model (indice en lista de modelos de antenas en model_file que se utiliza)
             i_model2 (indice en lista de modelos de llamadas en model_file que se utiliza)

    - Migrar modelos BD (comandos)
        Si se desea modificar los modelos sin borrar los datos ya insertados (definido en "manage.py"):

                        . venv/bin/activate
                        export APP_SETTINGS="config.DevelopmentConfig"

                        # crear historial de migraciones
                        flask db init
                        # instanciar los cambios
                        flask db migrate
                        # hacer "commit" de cambios
                        flask db upgrade

        (antes de esto hay que modificar el models.py, y después hacer los comandos "migrate" y "upgrade")