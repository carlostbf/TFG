# TFG
Detección de patrones y trayectorias a partir de información temporal y geoespacial poco precisa

TODO
    Leerme normativa
    Hacer diapositivas

    AFTERWARDS
        DATOS
            programar poder introducir fichero de datos y formatos (si no, quitar de requisitos)

            filtro carreteras
                necesito mejores datos
                ademas tendría que calcular velocidades
                Snap to roads
                trabajo futuro

            verificar que datos repetidos coinciden
        trayectorias movidas para que se vean (jitter)



MEMORIA
    objetivos       (HECHO)
        descripcion informal (hace esto con esto y tatata)
    requisitos      (HECHO)
        hay fichero, hace esto, etc
    estado arte     (HECHO)
    diseño (HECHO)
    DIFICULTADES ENCONTRADAS (HECHO)
    desarrollo
        diferencia con diseño?
            codigo alto nivel de cosas relevantes (algoritmos) mejor pseudo si no es simple
    integracion pruebas y resultados
        (setup inicial)
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



INFORMACIÓN SOBRE PLAZOS
    codigo
        evaluado por ortigosa principalmente
    memoria
        evaluan mi trabajo, no es un manual de usuario

    defiendo en julio

    domingo 16 fecha ultimo dia que me da feedback
    jueves 13 sería fecha limite de memoria

