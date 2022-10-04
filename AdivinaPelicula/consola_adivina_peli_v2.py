# -*- coding: utf-8 -*-

import random
import peliculas as pelis
import pistas_pelicula_v2 as info
import impresora_peliculas as impresora

def dar_info_pelis()->None:
    
   
    todas = pelis.crear_peliculas()
    
    #random nos permite generar números aleatorios
    #en este caso en un rango de 1 a 7
    num_peli_1 = random.randrange(1,len(todas),1)
    num_peli_2 = random.randrange(1,len(todas),1)
    num_peli_3 = random.randrange(1,len(todas),1)
    num_peli_4 = random.randrange(1,len(todas),1)
    
    
    p1 =  todas[num_peli_1]
    p2 =  todas[num_peli_2]
    p3 =  todas[num_peli_3]
    p4 =  todas[num_peli_4]
    
    print("")
    print("")
    print("="*10, "PELÍCULAS EN JUEGO","="*10)
    impresora.imprimir_pelicula(p1)
    print("="*10)
    impresora.imprimir_pelicula(p2)
    print("="*10)
    impresora.imprimir_pelicula(p3)
    print("="*10)
    impresora.imprimir_pelicula(p4)
    print("="*10)
    
    print("")
    print("")
    print("")
    
    print("¿Cuántas posteriores a 2000?", info.contar_cuantas_despues_2000(p1, p2, p3, p4))
    print("¿Cuántas animadas con calificacion de mas de 8.0?", info.contar_cuantas_animadas_mas_8(p1, p2, p3, p4))
    print("¿Alguna es animada?", info.hay_animada(p1, p2, p3, p4))
    print("¿Alguna es de comedia?", info.hay_comedia(p1, p2, p3, p4))
    print("¿Cómo se llama la más larga?", info.dar_nombre_mas_larga(p1, p2, p3, p4))
    print("¿Hay alguna repetida?", info.hay_repetida(p1, p2, p3, p4))
    print("¿Dar nombres dramas?", info.dar_de_drama(p1, p2, p3, p4))
    
    
dar_info_pelis()