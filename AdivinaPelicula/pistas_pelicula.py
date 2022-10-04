# -*- coding: utf-8 -*-

import peliculas 

peli = peliculas.crear_peliculas()[2]

def es_reciente(pelicula:dict)->bool:
    """
    Indica si la película es reciente. 
    Una película es reciente si es posterior a 2010

    Parameters
    ----------
    pelicula : dict
        película que se desea revisar

    Returns
    -------
    bool
        True si la película es reciente o False en caso contrario

    """
    #TODO revise como se responde a la pregunta es reciente
    return pelicula["anio"] > 2010



def es_buena(pelicula:dict)->bool:
    """
    Indica si la película es buena.
    Una película es buena si es animada y tiene una calificación mayor a 7.0
    o no es animada y tiene calificación mayor a 8.0

    Parameters
    ----------
    pelicula : dict
        película que se desea revisar

    Returns
    -------
    bool
        True si la película es buena o False en caso contrario

    """
    #TODO complete de acuerdo a la descripción
    return (pelicula["animada"] == True and pelicula["calificacion"] > 7.0) \
            or \
            (pelicula["animada"] == False and pelicula["calificacion"] > 8.0)



def es_para_todos(pelicula:dict)->bool:
    """
    Indica si la película es para todos.
    La película es para todos si es clasificacion PG

    Parameters
    ----------
    pelicula : dict
        película que se desea revisar

    Returns
    -------
    bool
        True si la película es para todos o False en caso contrario

    """
    #TODO complete de acuerdo a la descripción
    
    return pelicula["clasificacion"].upper() == "PG"



def da_pereza_verla(pelicula: dict)->bool:
    """
    Indica si da pereza ver la película.
    Da pereza ver una película cuando tiene duración y dura mas de 150 minutos 
    o cuando tiene una califiacion menor a 8.0
    
    Tenga en cuenta que algunas peliculas pueden no tener duración.

    Parameters
    ----------
    pelicula : dict
        La película que se desea revisar

    Returns
    -------
    bool
        True si da pereza ver la película o False en caso contrario

    """

    
    #La instrucción llave in dict nos permite saber 
    #si una lalve existe en un diccionario (True) o no (False)
    #tiene_duracion = "duracion" in pelicula
    
    tiene_duracion = pelicula.get("duracion") != None
    
    #TODO complete la función de acuerdo a la descripción
    return (tiene_duracion and pelicula["duracion"] > 150) \
            or pelicula["calificacion"] < 8.0




def es_bajo_costo(pelicula:dict)->bool:
    """
    Indica si la película es de bajo costo.
    Una película es de bajo costo, si su presupuesto mayor o igual a 35M y menor o igual a 175M

    Parameters
    ----------
    pelicula : dict
        La película que se desea revisar

    Returns
    -------
    bool
        True si la película es de bajo costo False de lo contrario

    """
    #TODO complete la función de acuerdo a la descripción
    #return 35000000 <= pelicula["presupuesto"] <= 175000000

    return pelicula["presupuesto"] >= 35000000 and \
            pelicula["presupuesto"] <= 175000000

def es_fracaso(pelicula: dict)->bool:
    """
    Indica si la película es un fracaso.
    Una película es un fracaso si su calificación es menor a 6 y su taquilla es menor al presupuesto

    Parameters
    ----------
    pelicula : dict
        La película que se desea revisar

    Returns
    -------
    bool
        True si la película es un fracaso False de lo contrario

    """
    #TODO complete la función de acuerdo a la descripción
    return pelicula["calificacion"] < 6 and pelicula["taquilla"] < pelicula["presupuesto"]

def sube_el_animo(pelicula: dict)->bool:
    """
    Indica si la película sube el animo del espectador.
    Una película sube el ánimo del espectador si su género es comedia o animada.
    Tenga en cuenta que la película puede no tener genero en este caso no sube el animo (False)

    Parameters
    ----------
    pelicula : dict
        La película que se desea revisar

    Returns
    -------
    bool
        True si la película sube el ánimo False de lo contrario

    """
    
    #La instrucción llave in dict nos permite saber 
    #si una lalve existe en un diccionario (True) o no (False)
    tiene_genero = "genero" in pelicula
    
    #TODO complete la función de acuerdo a la descripción
    return tiene_genero and (pelicula["genero"]== "Comedia" or pelicula["genero"]=="Animada")

def es_nombre_correcto(pelicula:dict, nombre_ingresado:str)->bool:
    """
    Indica si el nombre ingresado es igual al nombre de la película

    Parameters
    ----------
    pelicula : dict
        La película que se desea revisar
    nombre_ingresado : str
        El nombre con el que se desea comparar el nombre de la película

    Returns
    -------
    bool
        True si el nombre ingresado es igual al de la película o False en caso contrario

    """
    #TODO complete la función de acuerdo a la descripción
    return pelicula["nombre"] == nombre_ingresado