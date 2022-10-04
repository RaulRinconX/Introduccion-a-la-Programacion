# -*- coding: utf-8 -*-

def crear_pelicula(nombre: str, anio: int, es_animada: bool, \
                   calificacion_imdb:float, clasificacion:str, \
                   presupuesto:int, taquilla:int)->dict:
    """
    Crea un diccionario, que representa una pelicula, a partir de sus datos basicos, con
    la siguiente estructura:
    {"nombre":nombre,
     "anio":anio,
     "animada": es_animada,
     "calificacion":calificacion_imdb,
     "clasificacion":clasificacion,
     "presupuesto": presupuesto,
     "taquilla": taquilla}    
        

    Parameters
    ----------
    nombre : str
        nombre de la pelicula
    anio : int
        año de la pelicula
    es_animada : bool
        indica si la pelicula es animada o no
    calificacion_imdb : float
        califiacion de la pelicula segun imdb
    clasificacion : str
        clasificación de la pelicula
    presuesto : int
        presupuesto para filmar la película
    taquilla : int
        recaudación de la película

    Returns
    -------
    dict
        un diccionario con los datos de la pelicula

    """
    #TODO revise la creación del diccionario película
    pelicula = {    "nombre":nombre,
                    "anio":anio,
                    "animada": es_animada,
                    "calificacion":calificacion_imdb,
                    "clasificacion":clasificacion,
                    "presupuesto": presupuesto,
                    "taquilla": taquilla        
                }
    
    return pelicula


def agregar_duracion(pelicula: dict, duracion_minutos: int)->None:
    """
    Agrega a una pelicula su duracion en minutos

    Parameters
    ----------
    pelicula : dict
        pelicula a la que se desea agregar la duración
    duracion_minutos : int
        duracion de la pelicula en minutos


    """
    #TODO revise la adición de la característica duración al diccionario pelicula
    pelicula["duracion"] = duracion_minutos
    
def agregar_genero(pelicula:dict, genero:str)->None:
    """
    Agrega a una pelicula el genero

    Parameters
    ----------
    pelicula : dict
        pelicula a la que se desea agregar el personaje principal
    genero : str
        genero de la pelicula


    """
    #TODO complete agregando la característica genero al diccionario película
    pelicula["genero"] = genero
    
def agregar_numero_personajes(pelicula:dict, personajes:int)->None:
    """
    Agrega a la pelicula la cantidad de personajes

    Parameters
    ----------
    pelicula : dict
        pelicula a la que se le desea agregar la cantidad de personajes
    personajes : int
        cantidad de personajes de la pelicula

    """
     #TODO complete agregando la característica genero al diccionario cantidad_personajes
    pelicula["cantidad_personajes"] = personajes
    
    
def crear_peliculas()->dict:
    """
    Crea 5 peliculas para poder jugar y las agrega a un diccionario
    con llaves de 1 a 5

    Returns
    -------
    dict
        dicccionario que contiene 5 diccionarios que representan peliculas

    """
    pelicula1 = crear_pelicula("Titanic", 1997, False, 7.8, "PG-13", 200000000, 1845034188)
    agregar_genero(pelicula1, "Drama")
    agregar_duracion(pelicula1, 194)
    agregar_numero_personajes(pelicula1, 25)
    
    pelicula2 = crear_pelicula("Joker", 2019, False, 8.5, "PG", 70000000, 1074000000000)
    agregar_duracion(pelicula2, 122)
    
    pelicula3 = crear_pelicula("Mulan", 1998, True, 7.6, "PG", 90000000, 304320254)
    agregar_numero_personajes(pelicula3, 11)
    
    pelicula4 = crear_pelicula("Interestelar", 2014, False, 8.6, "PG-13", 165000000, 701000000)
    agregar_numero_personajes(pelicula4, 15)
    
    pelicula5 = crear_pelicula("Memento", 2000, False, 8.4, "R", 165000000, 701000000)
    agregar_genero(pelicula5, "Suspenso")
    
    pelicula6 = crear_pelicula("Up", 2009, True, 8.2, "PG", 175000000, 735099082)
    agregar_genero(pelicula6, "Animada")
    agregar_numero_personajes(pelicula6, 15)
    
    pelicula7 = crear_pelicula("Bandidas", 2006, False, 5.7, "PG-13", 35000000, 18000000)
    agregar_genero(pelicula7, "Comedia")
    
    peliculas = { 1: pelicula1,
                  2: pelicula2,
                  3: pelicula3,
                  4: pelicula4,
                  5: pelicula5,
                  6: pelicula6,
                  7: pelicula7
                }
    return peliculas
    
#TODO Comente esta línea al acabar este módulo
#print(crear_peliculas())