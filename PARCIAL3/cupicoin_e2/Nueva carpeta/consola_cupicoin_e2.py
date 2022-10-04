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

import cupicoin_e2 as cc
import time as t

def ejecutar_cargar_blockchain_cupicoin() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de las transacciones.
    Retorno: dict
        El diccionario de bloques con la informacion del archivo.
    """
    bloques = None
    archivo = input("Por favor ingrese el nombre del archivo CSV con las transacciones: ")
    bloques = cc.cargar_blockchain_cupicoin(archivo)
    if len(bloques) == 0:
        print("El archivo seleccionado no es valido. No se pudieron cargar los bloques.")
    else:
        print("Se cargaron los siguientes bloques a partir del archivo.")
        bls_n = ""
        for transaccion in bloques:
            bls_n += str(transaccion["numero_bloque"]) + ", "
        print(bls_n[:len(bls_n)-2])
    return bloques

def ejecutar_contar_menos_de_en_segmento(blockchain:list) -> None:
    """Ejecuta la opción de contar trnasacciones mayores a un valor dado en el segmento de bloques dado.
    """
    #TODO complete de acuerdo a la documentación
    b_inicial = int(input(print("Ingrese el bloque inicial: ")))
    b_final = int(input(print("Ingrese el bloque final: ")))
    valor = input(print("Ingrese el valor: "))
    contador = cc.contar_menos_de_en_segmento(blockchain, b_inicial, b_final, valor)
    
    print("la cantidad de transacciones son:", contador)
   

def ejecutar_existe_contrato_en_segmento(blockchain:list) -> None:
    """Ejecuta la opción de buscar un contrato en un segmento de bloques dado
    """
    #TODO complete de acuerdo a la documentación
    b_inicial = input(print("Ingrese el bloque inicial: "))
    b_final = input(print("Ingrese el bloque final: "))
    existe = cc.existe_contrato_en_segmento(blockchain, b_inicial, b_final)
    print("Existe un contrato en los segmentos?: ", existe)


def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar un archivo de transacciones.")
    print("2. Contar transacciones (tipo transferencia) menores a un valor en un segmento.")
    print("3. Buscar contrato en un segmento.")
    print("4. Salir.") 

def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    blockchain = []
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            blockchain = ejecutar_cargar_blockchain_cupicoin()
        elif opcion_seleccionada ==2:
            ejecutar_contar_menos_de_en_segmento(blockchain)
        elif opcion_seleccionada ==3:
            ejecutar_existe_contrato_en_segmento(blockchain)
        elif opcion_seleccionada == 4:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()