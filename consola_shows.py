# -*- coding: utf-8 -*-

import adminsitrador_shows as admin


def consola_dar_titulos_anio(shows:list)->None:
     anio = int(input("Ingrese el año que desea buscar: "))
     buscado = admin.dar_titulos_anio(shows, anio)
     print("="*30)
     print("Shows año " + str(anio))
     print(buscado)    
     print("="*30)
     
def consola_dar_titulos_clasificacion(shows:list)->None:
     clas = input("Ingrese la clasificación que desea buscar: ")
     buscado = admin.dar_titulos_clasificacion(shows, clas)
     print("="*30)
     print("Shows clasifiación " + clas)
     print(buscado)    
     print("="*30)
     
def consola_dar_titulo_anio_clasificacion(shows:list)->None:
     anio = int(input("Ingrese el año que desea buscar: ")) 
     clas = input("Ingrese la clasificación que desea buscar: ")
     
     buscado = admin.dar_titulo_anio_clasificacion(shows, anio, clas)
     print("="*30)
     print("Shows año y clasifiación " + str(anio) + "-" + clas)
     print(buscado)    
     print("="*30)
     
def dar_show_mayor_anio(shows:list)->None:
     buscado = admin.dar_show_mayor_anio(shows)
     print("="*30)
     print("Show mayor año")
     print(buscado)    
     print("="*30)
     
def dar_show_nombre_corto(shows:list)->None:
     buscado = admin.dar_show_nombre_corto(shows)
     print("="*30)
     print("Show nombre más corto")
     print(buscado)    
     print("="*30)
     
def dar_nombre_largo_anios(shows:list)->None:
     buscado = admin.dar_shows_nombre_largo(shows)
     print("="*30)
     print("Shows nombre largo por año")
     print(buscado)    
     print("="*30)
     

    
def iniciar_aplicacion():

    shows = admin.cargar()
    ejecutando = True
    while ejecutando:
        ejecutando = mostrar_menu_aplicacion(shows)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")


def mostrar_menu_aplicacion(shows: list) -> bool:
    
    print("Menu de opciones personajes")
    print(" 1 - Dar títulos por año: ")
    print(" 2 - Dar títulos por clasificación:")
    print(" 3 - Dar títulos por año y clasificación:")
    print(" 4 - Dar show mayo año")
    print(" 5 - Dar show nombre más corto")
    print(" 6 - Dar nombre largo por año")
    print(" 7 - Salir de la aplicacion.")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        consola_dar_titulos_anio(shows)
    elif opcion_elegida == "2":
        consola_dar_titulos_clasificacion(shows)
    elif opcion_elegida == "3":
        consola_dar_titulo_anio_clasificacion(shows)
    elif opcion_elegida == "4":
        dar_show_mayor_anio(shows)
    elif opcion_elegida == "5":
        dar_show_nombre_corto(shows)
    elif opcion_elegida == "6":
        dar_nombre_largo_anios(shows)
    elif opcion_elegida == "7":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    return continuar_ejecutando


iniciar_aplicacion()
