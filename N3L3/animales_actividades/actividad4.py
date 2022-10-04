# -*- coding: utf-8 -*-
import cargador_animales as c

def mamiferos_domesticos(animales:list)->list:
    """
    Crea y devuelve una lista que contiene los nombres
    de los animales mamiferos domesticos registrados
    en la lista de aniamales. Una animales es mamifero
    si el atributo "class_type" es "Mammal". Una animal
    es doméstico si el atributo "domestic" es True.
    El nombre del animal se encuentra guardado en el
    atributo "animal_name".

    Parameters
    ----------
    animales : list
        lista de disccionarios de animales.

     Returns
    -------
    list
        lista con los nombres de los animales mamiferos domesticos.

    """
    



l = c.cargar_animales("zoo.csv")
print("Mamiferos domesticos = ")
print(mamiferos_domesticos(l))
