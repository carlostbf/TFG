# TFG
Detección de patrones y trayectorias a partir de información temporal y geoespacial poco precisa

TODO
    CODIGO
        MAPAS
            pintar trayectoria por numeros de tlf
                (ahora mismo es por antenas)
                añadir filtro por tiempo

            dado un area obtener telefonos cercanos
                pintar trayectorias?

        programar poder introducir fichero de datos y formatos

DUDAS
    interfaz cargado datos
        la tengo que hacer?

    pintar trayectoria por numeros de tlf
        filtro para tlf_o y tlf_d (debería ser solo tlf)
        solo uso ubicación de antenas
        añadir filtro de tiempo

    dado un area obtener telefonos cercanos
        pintar trayectorias de cada movil
            como debería hacerlo?
        ahora mismo es buscar antenas que tienen rango de alcance solapado con rango del filtro


    No sé si puedo hacer filtro carreteras
        necesito mejores datos
        ademas tendría que calcular velocidades
        Snap to roads

    dejar el código bonito comentado y bien modulado

    MEMORIA
        contar como montar todo la aplicación?
        presentación la hago despues de entrega?


MEMORIA
    objetivos <-------------------------------------------------
        descripcion informal (hace esto con esto y tatata)
    requisitos <-------------------------------------------------
        hay fichero, hace esto, etc
    estado arte
        pros y contras de tecnologias en estado arte
    diseño
        decidir tecnologias
    DIFICULTADES ENCONTRADAS <-------------------------------------------------
        CAMBIAR A GOOGLE MAPS
            explicar razones
        Simular Datos
    desarrollo <-------------------------------------------------
        versiones de herramientas
        detalles sobre como se ha implementado?
        diferencia con diseño?
            codigo alto nivel de cosas relevantes (algoritmos) mejor pseudo si no es simple
    integracion pruebas y resultados
        setup inicial
        explicar como usar aplicación
        capturas de pantalla
    trabajo futuro
        bootstrap

ALGORITMO
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
            filtro descartar rutas carreteras (gente que pasa muy rapido por la zona) (registro de llamadas)
            descartar por filtros de tiempo quien ha estado mas tiempo (me interesa por si estan haciendo algo ilegal).
            teniendo en cuenta que no se apagan
            puede haberlo apagado (no descartarlo?)

        ii) Determinar trayectorias y posibles coincidencias de localización de un teléfono específico
            dado telefono e instantes => encontrar su trayectoria
            pueden ser mas de x telefonos a la vez

            ver a quienes llama el sospechoso
            ver la red de llamadas a sospechosos


EXTRAS
    requirements.txt
    .env para Variables de entorno automaticas
    aplicación tiene que ser instalable? concentrarme en codigo
        pip install?
        script?

    (geolocation permite, a partir de ip, obtener pubs más cercanos
	integrar postgres en python)


INFORMACIÓN SOBRE PLAZOS
    codigo
        evaluado por ortigosa principalmente
    memoria
        evaluan mi trabajo, no es un manual de usuario

    envio de memoria por capitulo cerrado
    memoria final para ortigosa 15 dias antes
    defiendo en julio


COMANDOS
    export APP_SETTINGS="config.DevelopmentConfig"
    flask db init
    flask db migrate
    flask db upgrade


