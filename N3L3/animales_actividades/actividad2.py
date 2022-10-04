# -*- coding: utf-8 -*-
import cargador_animales as c

def mamiferos(animales:list)->int:
    """
    Calcula y devuelve la cantidad de mamiferos registrados
    en la lista de animales. Un animal es mamifero si
    su atributo "class_type" es igual a "Mammal"

    Parameters
    ----------
    animales : list
        Lista de diccionarios de aniamles

    Returns
    -------
    int
        Cantidad de animales mamiferos en la lista

    """
    



l = c.cargar_animales("zoo.csv")
print("Cant. mamiferos = ", str(mamiferos(l)))