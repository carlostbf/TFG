# TFG
Detección de patrones y trayectorias a partir de información temporal y geoespacial poco precisa

TODO
    GMAPS
        nearest roads
            array de puntos

    HACER FORMULARIO PARA FILTROS EN WEB

    INVESTIGAR JSON PARA CREAR FORMATOS DE CSV EN BBDD


DIFICULTADES ENCONTRADAS
    CAMBIAR A GOOGLE MAPS


COMANDOS
    export APP_SETTINGS="config.DevelopmentConfig"


EXTRAS
    requirements.txt
    .env para Variables de entorno automaticas
    aplicación tiene que ser instalable? concentrarme en codigo
        pip install?
        script?

    (geolocation permite, a partir de ip, obtener pubs más cercanos
	integrar postgres en python)




PREGUNTAS
    he cambiado a maps

    algoritmo para trayectorias?(telefonos por antenas)
        ver areas donde se encuentra telefono
            descartar posibilidades?

        como son los filtros/consultas?
            maps me da carretera mas cercana a un punto
            distancias necesarias?

        trayectorias posibles
            solo caminando? o tambien carreteras usadas?

    Como simular datos?
        (tengo datos de antenas de opencellid)
        telefono + tiempos + (varias antenas asociadas en una misma zona)
        en general no se como hacerlo realista


    memoria (registro y contenido)
        objetivos?
            igual que requisitos?
        estado arte
            decidir tecnologias en diseño o estado arte?
        desarrollo
            detalles sobre como se ha implementado?
            diferencia con diseño?
        integracion pruebas y resultados
            capturas de pantalla


    en general, criterios para correccion?
        codigo
        memoria

    defiendo en julio