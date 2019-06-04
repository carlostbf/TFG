# TFG
Detección de patrones y trayectorias a partir de información temporal y geoespacial poco precisa

TODO
    PENSAR TODAS LAS INTERACCIONES DE LA PÁGINA WEB
    filtro de tiempo en ambos casos? 2 sliders independientes
    CODIGO
        MAPAS
            pintar trayectoria por numeros de tlf
                filtros de mas de x minutos
                    slider de tiempo para mostrar telefonos que han estado con objetivo en esos intervalos
                dado 1 numero telefono lista de zonas donde estuvo
                del resto telefonos cuales han compartido más de una ubicación con el objetivo

            dado un area obtener telefonos cercanos
                pintar trayectorias? NO
                filtro tiempo estancia (cuanto tiempo ha estado allí) 0-2h?
                (seleccionar telefono en tabla y mostrar ubicacion asociada)

    AFTERWARDS
        DATOS
            programar poder introducir fichero de datos y formatos (si no, quitar de requisitos)

            filtro carreteras
                necesito mejores datos
                ademas tendría que calcular velocidades
                Snap to roads
                trabajo futuro

            verificar que datos repetidos coinciden
            mejorar interfaz datetime

DUDAS

    pintar trayectoria por numeros de tlf
        filtro para tlf_o y tlf_d (debería ser solo tlf) si
        solo uso ubicación de antenas (sí)
        añadir filtro de tiempo


    dejar el código bonito comentado y bien modulado

    MEMORIA
        contar como montar todo la aplicación?
        presentación la hago despues de entrega?








MEMORIA
    objetivos       (HECHO)
        descripcion informal (hace esto con esto y tatata)
    requisitos      (HECHO)
        hay fichero, hace esto, etc
    estado arte     (HECHO)
        pros y contras de tecnologias en estado arte
    diseño (CASI)
        decidir tecnologias
    DIFICULTADES ENCONTRADAS
        CAMBIAR A GOOGLE MAPS
            explicar razones
        Simular Datos
    desarrollo
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


INFORMACIÓN SOBRE PLAZOS
    codigo
        evaluado por ortigosa principalmente
    memoria
        evaluan mi trabajo, no es un manual de usuario

    (envio de memoria por capitulo cerrado)
    defiendo en julio

    concentrarme en interfaz
    memoria
    luego acabo codigo

    domingo 16 fecha ultimo dia que me da feedback
    jueves 13 sería fecha limite de memoria


COMANDOS
    export APP_SETTINGS="config.DevelopmentConfig"
    flask db init
    flask db migrate
    flask db upgrade


