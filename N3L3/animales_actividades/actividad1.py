# -*- coding: utf-8 -*-
import cargador_animales as c

def cuantos_animales(animales:list)->int:
    """
    Permite conocer la cantidad de animales registrados en la lista que llega
    por parámetro

    Parameters
    ----------
    animales : list
        lista de diccionarios de animales

    Returns
    -------
    int
        cantidad de animales en la lista

    """
    contar = 0
    for i in animales:
        contar += 1
    
    return contar


def primer_animal(animales:list)->dict:
    """
    Devuelve el diccionario del primer animal de la lista 
    que llega por parámetro

    Parameters
    ----------
    animales : list
        lista de diccionarios de aniamles

    Returns
    -------
    dict
        el primer diccionario de la lista

    """
    primero = animales[0]
    return primero
        
	

def ultimo_animal(animales:list)->dict:
    """
    Devuelve el diccionario del último animal de la lista 
    que llega por parámetro

    Parameters
    ----------
    animales : list
        lista de diccionarios de aniamles

    Returns
    -------
    dict
        el último diccionario de la lista

    """
    ultimo = animales[len(animales) - 1]
    return ultimo
	

def animal_50(animales:list)->dict:
    """
    Devuelve el diccionario 50 de la lista
    que llega por parámetro

    Parameters
    ----------
    animales : list
        lista de diccionarios de aniamles

    Returns
    -------
    dict
        el diccionario 49 de la lista

    """
    cincuenta = animales[49]
    return cincuenta
    
    

def ultimos3(animales:list)->list:
    """
    Devuelve una lista con los últimos 3 diccionarios
    de la lista de animales

    Parameters
    ----------
    animales : list
        lista de diccionarios de aniamles

    Returns
    -------
    dict
        lista con los últimos 3 diccionarios de la lista 
        de animales

    """
    
	

l = c.cargar_animales("zoo.csv")
print("cantidad = ", cuantos_animales(l))
print("\nprimero = ", primer_animal(l))
print("\nultimo = ", ultimo_animal(l))
print("\n50 = ", animal_50(l))
print("\núltimos 5 = ", ultimos3(l))