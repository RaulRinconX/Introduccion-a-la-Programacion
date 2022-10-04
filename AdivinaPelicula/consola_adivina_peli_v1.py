# -*- coding: utf-8 -*-

import random
import peliculas as pelis
import pistas_pelicula as pistas
import impresora_peliculas as impresora

def adivinar_pelicula()->None:
    
   
    todas = pelis.crear_peliculas()
    
    #random nos permite generar números aleatorios
    #en este caso en un rango de 1 a 7
    num_peli = random.randrange(1,len(todas),1)
    
    
    peli =  todas[num_peli]
    
    print("")
    print("")
    print("="*10, "Pistas","="*10)
    print("¿es reciente?", pistas.es_reciente(peli))
    print("¿es buena?", pistas.es_buena(peli))
    print("¿es para todos?", pistas.es_para_todos(peli))
    print("¿da pereza verla?", pistas.da_pereza_verla(peli))
    print("¿es bajo costo?", pistas.es_bajo_costo(peli))
    print("¿es fracaso?", pistas.es_fracaso(peli))
    print("¿Sube el ánimo?", pistas.sube_el_animo(peli))
    
    print("")
    resp = input("Ingrese el nombre de la pelicula: ")
    
    print("")
    print("")
    print("="*10, "Resultado","="*10)
    print("¿adivinaste?", pistas.es_nombre_correcto(peli, resp))
    print("La película era:")
    impresora.imprimir_pelicula(peli)
    
adivinar_pelicula()