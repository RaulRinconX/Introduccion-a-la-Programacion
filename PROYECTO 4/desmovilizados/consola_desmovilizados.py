import desmovilizados_esqueleto as funciones
import pandas as pd


def ejecutar_cargar_datos():
    """Solicita al usuario que ingrese el nombre de un archivo CSV con la informacion
    Retorno: dict
        El dataframe con la informacion del archivo.
    """
    archivo = input("Por favor ingrese el nombre del archivo CSV: ")
    dataframe = funciones.cargar_datos(archivo)
    print("Datos cargandos correctamente...!!")
    return dataframe

def ejecutar_crear_matriz(datos: pd.DataFrame)->tuple:
    return funciones.crear_matriz(datos)

def ejecutar_desmovilizados_grupo_armado(datos:pd.DataFrame)->None:
    funciones.desmovilizados_grupo_armado(datos)
    print("Se ha graficado los desmovilizados según grupo armado.")

def ejecutar_numero_desmovilizados_rango_años(datos:pd.DataFrame)->None:
    anio_menor = int(input("Ingrese el año menor: "))                 
    anio_mayor = int(input("Ingrese el año mayor: "))
    funciones.numero_desmovilizados_rango_años(datos, anio_menor, anio_mayor)
    
def ejecutar_departamentos_mayor_desmovilizados(datos:pd.DataFrame)->None:
    desmovilizacion = input("Ingrese el tipo de desmovilización: ")
    funciones.departamentos_mayor_desmovilizados(datos, desmovilizacion)

def ejecutar_segun_numero_de_hijos_y_sexo(datos:pd.DataFrame)->None:
    funciones.segun_numero_de_hijos_y_sexo(datos)
    
def ejecutar_ocupacion_individuos_beneficio_desembolso(datos:pd.DataFrame)->None:
    funciones.ocupacion_individuos_beneficio_desembolso(datos)
    
def ejecutar_grupo_mas_desmovilizados_por_departamento(tupla: tuple)->None:
    departamento = input("Ingrese el departamento que desea mirar: ")
    resultado = funciones.grupo_mas_desmovilizados_por_departamento(tupla, departamento)
    print("El ex grupo con mas desmovilizados en", departamento,"es", resultado)
    
def ejecutar_contar_personas_por_grupo(tupla: tuple)->None:
    resultado = funciones.departamento_grupo_mayor_desmovilizados(tupla)
    print("El departamento y grupo armado con mayor cantidad de desmovilizados son: ", resultado)
    
def ejecutar_grupo_mayor_desmovilizacion_departamento(tupla: tuple)->None:
    resultado = funciones.grupo_mayor_desmovilizacion_departamento(tupla)
    print("El departamento y grupo que tuvo mayor número de desmovilizados fue", resultado)

def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Graficar distribución de los desmovilizados según grupo armado.")
    print("2. Graficar tendencia del número de desmovilizados por un rango de años.")
    print("3. Graficar top 5 departamentos por tipo de desmovilización (Individual o Colectiva).")
    print("4. Graficar según distribución del número de hijos que tienen los desmovilizados según su sexo.")
    print("5. Graficar la distribución de las ocupaciones de los individuos que hayan tenido acceso a cualquier tipo de beneficio o desembolso.")
    print("6. Contar personas por grupo y departamento.")
    print("7. Departamento y ex grupo armado con mayor cantidad de desmovilizados.")
    print("8. Ex grupo con mayor desmovilización por departamento.")
    print("9. Salir.") 
    
    
def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    datos = ejecutar_cargar_datos()
    tupla = ejecutar_crear_matriz(datos)
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            ejecutar_desmovilizados_grupo_armado(datos)
        elif opcion_seleccionada == 2:
            ejecutar_numero_desmovilizados_rango_años(datos)
        elif opcion_seleccionada == 3:
            ejecutar_departamentos_mayor_desmovilizados(datos)
        elif opcion_seleccionada == 4:
            ejecutar_segun_numero_de_hijos_y_sexo(datos)
        elif opcion_seleccionada == 5:
            ejecutar_ocupacion_individuos_beneficio_desembolso(datos)
        elif opcion_seleccionada == 6:
            ejecutar_grupo_mas_desmovilizados_por_departamento(tupla)
        elif opcion_seleccionada == 7:
            ejecutar_contar_personas_por_grupo(tupla)
        elif opcion_seleccionada == 8:
            ejecutar_grupo_mayor_desmovilizacion_departamento(tupla)
        elif opcion_seleccionada == 9:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()