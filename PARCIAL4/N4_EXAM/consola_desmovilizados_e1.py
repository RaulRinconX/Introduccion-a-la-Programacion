"""
Ejercicio nivel 3: Blockchain de Cupicoin.
Interfaz basada en consola para la interaccion con el usuario.

Temas:
* Instrucciones repetitivas.
* Listas
* Diccionarios
* Archivos
@author: Cupi2
"""
import pandas as pd
import desmovilizados_e1 as dd

def ejectuar_graficar_situacion_proceso(datos: pd.DataFrame)->None:
    dd.graficar_situacion_proceso(datos)
    print("Se ha graficado la cantidad de desmovilziados por situación en el proceso")
    
    
def ejecutar_dar_desmovilizados_grupo_anio(datos: pd.DataFrame)->None:
    
    grupo = input("Ingrese el nombre del grupo que desea consultar: ")
    grupo = grupo.upper().strip()
    cant = len(datos[ datos["ExGrupo"] == grupo ])
    if cant == 0:
        print("El grupo ingresado no se encuentra registrado en el dataframe")
    else:
        print("Para el grupo " + grupo + " se presentan los siguientes desmovilizados por año: ")
        print(dd.dar_desmovilizados_grupo_anio(datos, grupo))

def ejecutar_desmovilizados_por_sexo_situacion(datos: pd.DataFrame)->None:
    
    info_matriz = dd.crear_matriz(datos)
    sexo = input("Ingrese el sexo " + str(list(info_matriz[0].keys())) + " que desea consultar: ")
    sexo = sexo.upper().strip()
    
    situacion =  input("Ingrese la situación que desea " + str(list(info_matriz[1].keys()) ) + " que desea consultar: ")
    situacion = situacion.strip()
    
    print("La cantidad de desmovilizados del sexo " +  sexo + " en la situación " + situacion + " es: ")
    print(dd.dar_desmovilizados_por_sexo_situacion(info_matriz, sexo, situacion))
        


def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Graficar desmovilizados por situacion del proceso.")
    print("2. Dar desmovilizados por grupo y año.")
    print("3. Dar desmovilizados por sexo y estado.")
    print("4. Salir.") 

def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    datos = dd.cargar_datos()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
             ejectuar_graficar_situacion_proceso(datos)
        elif opcion_seleccionada ==2:
            ejecutar_dar_desmovilizados_grupo_anio(datos)
        elif opcion_seleccionada ==3:
            ejecutar_desmovilizados_por_sexo_situacion(datos)
        elif opcion_seleccionada == 4:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()