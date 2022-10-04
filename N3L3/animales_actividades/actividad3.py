# -*- coding: utf-8 -*-
import cargador_animales as c

def mamiferos_acuaticos(animales:list)->int:
    """
    Calcula y devuelve la cantidad de animales mamiferos
    acuaticos registrados en la lista de aniamles. Un 
    animal es mamifero si su atributo "class_type" es igual
    a "Mammal". Una animal es acuatico si su atributo
    "aquatic" es True

    Parameters
    ----------
    animales : list
        lista de diccionarios de animales

    Returns
    -------
    int
        cantidad de mamiferos acuaticos en la lista de aniamles

    """
    



l = c.cargar_animales("zoo.csv")
print("Cant. mamiferos acuáticos = ", str(mamiferos_acuaticos(l)))
