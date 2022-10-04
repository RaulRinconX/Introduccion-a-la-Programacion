# -*- coding: utf-8 -*-


def contar_cuantas_despues_2000(p1:dict, p2:dict, p3:dict, p4:dict)->int:
    """
    Indica cuantas películas de las 4 que llegan por parámetro 
    salieron después del 2000

    Parameters
    ----------
    p1 : dict
        Película 1 para revisar
    p2 : dict
         Película 2 para revisar.
    p3 : dict
         Película 3 para revisar.
    p4 : dict
         Película 4 para revisar.

    Returns
    -------
    int
        Devuelve la cantidad de películas que salieron después del
        2000.

    """
    #TODO Reemplace la siguiente línea con su implementación
    cantidad = 0
    
    if (p1["anio"] > 2000) == True:
        cantidad += 1
    if (p2["anio"] > 2000) == True:
        cantidad += 1
    if (p3["anio"] > 2000) == True:
        cantidad += 1
    if (p4["anio"] > 2000) == True:
        cantidad += 1
    return cantidad

def contar_cuantas_animadas_mas_8(p1:dict, p2:dict, p3:dict, p4:dict)->int:
    """
    Indica cuantas películas de las 4 que llegan por parámetro 
    son animadas y tienen calificación mayor a 8.0

    Parameters
    ----------
    p1 : dict
        Película 1 para revisar
    p2 : dict
         Película 2 para revisar.
    p3 : dict
         Película 3 para revisar.
    p4 : dict
         Película 4 para revisar.

    Returns
    -------
    int
        Devuelve la cantidad de películas que son animadas
        y tienen calificación mayor a 8.0

    """
    #TODO Reemplace la siguiente línea con su implementación ["animada"] ["calificacion"] 
    cantidad = 0
    if p1["animada"] == True and p1["calificacion"] > 8.0:
        cantidad += 1
    if p2["animada"] == True and p2["calificacion"] > 8.0:
        cantidad += 1
    if p3["animada"] == True and p3["calificacion"] > 8.0:
        cantidad += 1
    if p4["animada"] == True and p4["calificacion"] > 8.0:
        cantidad += 1
    return cantidad

def hay_animada(p1:dict, p2:dict, p3:dict, p4:dict)->bool:
    """
    Indica si entre las 4 películas por parámetro hay una animada

    Parameters
    ----------
    p1 : dict
        Película 1 para revisar
    p2 : dict
         Película 2 para revisar.
    p3 : dict
         Película 3 para revisar.
    p4 : dict
         Película 4 para revisar.

    Returns
    -------
    bool
        True si hay al menos una película animada entre las
        4 películas o False en caso contrario.

    """
    #TODO Reemplace la siguiente línea con su implementación
    return p1["animada"] == True or p2["animada"] == True or p3["animada"] == True or p4["animada"] == True

def hay_comedia(p1:dict, p2:dict, p3:dict, p4:dict)->bool:
    """
    Indica si entre las 4 películas por parámetro hay una de genero Comedia

    Parameters
    ----------
    p1 : dict
        Película 1 para revisar
    p2 : dict
         Película 2 para revisar.
    p3 : dict
         Película 3 para revisar.
    p4 : dict
         Película 4 para revisar.

    Returns
    -------
    bool
        True si hay al menos una película de comedia entre las
        4 películas o False en caso contrario.

    """
    tiene_genero = "genero" in p1, p2, p3, p4
    #TODO Reemplace la siguiente línea con su implementación
    return tiene_genero == "Comedia" 

def dar_nombre_mas_larga(p1:dict, p2:dict, p3:dict, p4:dict)->str:
    """
    Indica el nombre de la película con mayor duración
    entre las 4 películas por parámetro

    Parameters
    ----------
    p1 : dict
        Película 1 para revisar
    p2 : dict
         Película 2 para revisar.
    p3 : dict
         Película 3 para revisar.
    p4 : dict
         Película 4 para revisar.

    Returns
    -------
    str
        Nombre de la película con mayor duración
        entre las 4 películas por parámetro

    """
    duracion_p1 = "duracion" in p1
    duracion_p2 = "duracion" in p2
    duracion_p3 = "duracion" in p3
    duracion_p4 = "duracion" in p4
    #TODO Reemplace la siguiente línea con su implementación
    if (duracion_p2 and duracion_p3 and duracion_p4 < duracion_p1):
        return p1["nombre"]
    if (duracion_p1 and duracion_p3 and duracion_p4 < duracion_p2):    
        return p2["nombre"]
    if (duracion_p2 and duracion_p1 and duracion_p4 < duracion_p3):
        return p3["nombre"]
    if (duracion_p2 and duracion_p1 and duracion_p3 < duracion_p4):
        return p4["nombre"]
    


def hay_repetida(p1:dict, p2:dict, p3:dict, p4:dict)->bool:
    """
    Indica si entre las 4 pelícuas por parámetro 
    hay un par que tienen el mismo nombre (hay repetidas)

    Parameters
    ----------
    p1 : dict
        Película 1 para revisar
    p2 : dict
         Película 2 para revisar.
    p3 : dict
         Película 3 para revisar.
    p4 : dict
         Película 4 para revisar.

    Returns
    -------
    bool
        True si hay repetidas o False en caso contrario

    """
    #TODO Reemplace la siguiente línea con su implementación
    
    if(p1["nombre"] == p2["nombre"] == p3["nombre"] == p4["nombre"] ):
        return True
    
    

  


def dar_de_drama(p1:dict, p2:dict, p3:dict, p4:dict)->str:
    
    """
    Devuelve una cadena de caractéres (str) con el nombre de
    todas las películas de Drama, de las 4 peliculas por parámetro.
    Los nombres deben estar separados por coma.
    Por ejemplo:
        Chichas pesadas, La Momia
    En caso que no haya películas de drama, devuelve el mensaje
    <No hay de drama>
        

    Parameters
    ----------
    p1 : dict
        Película 1 para revisar
    p2 : dict
         Película 2 para revisar.
    p3 : dict
         Película 3 para revisar.
    p4 : dict
         Película 4 para revisar.

    Returns
    -------
    str
        Nombres de las películas de Drama.

    """
    respuesta = ""
    genero_p1 = "genero" in p1
    genero_p2 = "genero" in p2
    genero_p3 = "genero" in p3
    genero_p4 = "genero" in p4
     
    #TODO complete con su implementación
    
    if genero_p1 == "Drama":
         respuesta += ","+ p1["nombre"]    
    
    if  genero_p2 == "Drama":
        respuesta += ","+ p2["nombre"]    
    
    if genero_p3 == "Drama":
        respuesta += ","+ p3["nombre"]    
    
    if genero_p4 == "Drama":
        respuesta += ","+ p4["nombre"]
    if respuesta == "":
        respuesta = "No hay drama"
    
    return respuesta