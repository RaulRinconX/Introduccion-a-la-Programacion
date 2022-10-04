# -*- coding: utf-8 -*-
import cargador_animales as c

def domestico_oviparo(animales:list)->bool:
    """
    Indica si en la lista de animales hay animales
    oviparos domesticos. Una animal es oviparo
    si el atributo "eggs" es True. Una animal es 
    domestico si el atributo "domestic" es True.

    Parameters
    ----------
    animales : list
        lista de diccionarios de animales

    Returns
    -------
    bool
        True si la lista contiene animales 
        oviparos domesticos o False en 
        caso contrario.

    """
    



l = c.cargar_animales("zoo.csv")
print("¿Hay domesticos oviparos? = ", str(domestico_oviparo(l)))
