# -*- coding: utf-8 -*-

import peliculas

def imprimir_pelicula(pelicula:dict)->None:
    """
    Imprime la información de una pelicula que llega por parámetro

    Parameters
    ----------
    pelicula : dict
        Diccionario con la información de la película. 
        El diccionario tendrá la estructura
                {   "nombre": <nombre>,
                    "anio":<anio>,
                    "animada": <es_animada>,
                    "calificacion":<calificacion_imdb>,
                    "clasificacion":<clasificacion>,
                    "presupuesto": <presupuesto>,
                    "taquilla": <taquilla>        
                }

        Algunas películas pueden tener las llaves duracion, genero, cantidad_personajes

    """
    print("="*20)
    print("NOMBRE:\t\t\t" + pelicula["nombre"] )
    print("AÑO:\t\t\t" + str(pelicula["anio"]))
    
    #TODO imprima las características animada, calificacion, 
    #clasifaicacion, presupuesto y taquilla de la película
    print("¿ES ANIMADA?:\t\t" + str(pelicula["animada"]))
    print("CALIFICACIÓN:\t\t" + str(pelicula["calificacion"]))
    print("CLASIFICACIÓN:\t\t" + str(pelicula["clasificacion"]))
    print("PRESUPUESTO:\t\t" + str(pelicula["presupuesto"]))
    print("TAQUILLA:\t\t" + str(pelicula["taquilla"]))
    
    #TODO revise la impresión de las carácterísticas duracion, genero y cantidad_personajes
    #pruebe imprimir varias películas y analice el funcionamiento de la instrucción get cuando 
    #la llave solicitada no existe en el diccionario
    print("DRUACIÓN:\t\t" + str(pelicula.get("duracion")))
    print("GÉNERO:\t\t\t" + str(pelicula.get("genero")))
    print("# PERSONAJES:\t\t" + str(pelicula.get("cantidad_personajes")))
    

#TODO comente o descomente estás líneas para probar la impresión de películas
#Una vez haya completado este modulo deje todas estás líneas comentadas
#imprimir_pelicula(peliculas.crear_peliculas()[1])
#imprimir_pelicula(peliculas.crear_peliculas()[2])
#imprimir_pelicula(peliculas.crear_peliculas()[3])
#imprimir_pelicula(peliculas.crear_peliculas()[4])
#imprimir_pelicula(peliculas.crear_peliculas()[5])
#imprimir_pelicula(peliculas.crear_peliculas()[6])


#peli = peliculas.crear_peliculas()[2]
#print(peli)

#tiene_llave = "genero"  in peli  #\t


#print(tiene_llave)




