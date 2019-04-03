# TFG
Detección de patrones y trayectorias a partir de información temporal y geoespacial poco precisa

TODO
    CODIGO
        GMAPS
            nearest roads
                array de puntos

        HACER FORMULARIO PARA FILTROS EN WEB

        INVESTIGAR JSON PARA CREAR FORMATOS DE CSV EN BBDD

    MEMORIA
        Ampliar Estado del arte
        Dificultades encontradas

DIFICULTADES ENCONTRADAS
    CAMBIAR A GOOGLE MAPS
        explicar razones


COMANDOS
    export APP_SETTINGS="config.DevelopmentConfig"
    flask db init
    flask db migrate
    flask db upgrade

EXTRAS
    requirements.txt
    .env para Variables de entorno automaticas
    aplicación tiene que ser instalable? concentrarme en codigo
        pip install?
        script?

    (geolocation permite, a partir de ip, obtener pubs más cercanos
	integrar postgres en python)




PREGUNTAS
    algoritmo para trayectorias?(telefonos por antenas)
        ver areas donde se encuentra telefono (algoritmo probabilistico?)
            descartar posibilidades? con filtros

        como son los filtros/consultas?
            maps me da carretera mas cercana a un punto
            distancias necesarias? las puedo calcular

        trayectorias posibles
            solo caminando? o tambien carreteras usadas?

        i) Determinar patrón de comportamiento de todos los teléfonos detectados en un área determinada
            -dado area e instantes => mostrar telefonos y trayectorias
            filtro descartar rutas carreteras (gente que pasa muy rapido por la zona)
            descartar por filtros de tiempo quien ha estado mas tiempo (me interesa por si estan haciendo algo ilegal).

        ii) Determinar trayectorias y posibles coincidencias de localización de un teléfono específico
            dado telefono e instantes => encontrar su trayectoria
            pueden ser mas de x telefonos a la vez


    Como simular datos?
        (tengo datos de antenas de opencellid)
        telefono + tiempos + (varias antenas asociadas en una misma zona)
            antenas + ventanas de tiempo + telefonos + areas de antenas
                interpolacion probabilistica

        en general no se como hacerlo realista
            espero hasta 5 abril para datos como mucho


    memoria (registro y contenido)
        objetivos?
            descripcion informal (hace esto con esto y tatata)
        requisitos
            hay fichero, hace esto, etc
        estado arte
            pros y contras en estado arte
            decidir tecnologias en diseño o estado arte?
                diseño
            explayarme con explicaciones neo4J
        desarrollo
            detalles sobre como se ha implementado?
            diferencia con diseño?
                codigo alto nivel de cosas relevantes (algoritmos) mejor pseudo si no es simple
        integracion pruebas y resultados
            capturas de pantalla


    en general, criterios para correccion?


INFORMACIÓN SOBRE PLAZOS
    codigo
        evaluado por ortigosa principalmente
    memoria
        evaluan mi trabajo, no es un manual de usuario

    envio de memoria por capitulo cerrado
    memoria final para ortigosa 15 dias antes
    defiendo en julio

DATOS
    ignorar columnas irrelevantes
    intentar unificar ficheros en uns sola tabla
    cuando populo?
        cargado acumulado
        detectar repetidos
    uso datos de opencellid??
        si siempre que se pueda
    formatos??
        dates asumir algo y luego cambiarlo en el descriptor
        predefinidos
    TODO
        ignorar duplicated key
        study SQLalchemy datetime formats
