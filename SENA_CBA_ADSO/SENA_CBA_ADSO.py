# *
# Centro de biotecnologia agropecuaria
# Ficha: 2877795
# Aprendiz: Bryan Muñoz
# Version: Python312
# Fecha: 14/05/2024
# *
"""
Este programa nos sirve para registrar aprendices y tener sus datos
ver todos los aprendices que tenemos en total y por ficha
ademas de eso ver quienes aprobaron y desaprobaron la materia
"""
from colorama import Fore, Style, init


# Inicializa Colorama
init(autoreset=True)
aprendices = []

def registrar_aprendiz():
    """
    Esta función permite registrar un nuevo aprendiz. Solicita al usuario que ingrese el documento, nombre, evaluación y ficha del aprendiz.
    La evaluación debe ser 'A' para aprobado o 'D' para desaprobado. Los datos del aprendiz se guardan en la lista global 'aprendices'.
    """
    while True:  # Agregamos un bucle while aquí
        documento = input("Ingrese el documento: ")
        nombre = input("Ingrese el nombre y apellidos: ")
        evaluacion = ""
        while evaluacion.lower() not in ["a", "d"]:
            evaluacion = input("Ingrese la evaluación (A para aprobado, D para desaprobado): ")
        ficha = input("Ingrese la ficha: ")
        aprendices.append({"documento": documento, "nombre": nombre, "evaluacion": evaluacion, "ficha": ficha})
        print(f"Aprendiz {nombre} registrado con éxito.")  # Confirmación de que el aprendiz se ha registrado
        otro = input("¿Desea ingresar otro aprendiz? (S/N): ")
        if otro.lower() != "s":
            break  # Si el usuario responde algo distinto a "s", rompemos el bucle

def listar_aprendices():
    """
    Esta función imprime en consola todos los aprendices registrados.
    """
    for aprendiz in aprendices:
        print("------------------------")
        print(f"Documento: {aprendiz['documento']}")
        print(f"Nombre: {aprendiz['nombre']}")
        print(f"Evaluación: {aprendiz['evaluacion']}")
        print(f"Ficha: {aprendiz['ficha']}")
        print("------------------------")

def listar_ficha():
    """
    Esta función imprime en consola todas las fichas existentes sin repetir y los datos de cada aprendiz.
    """
    fichas = set()
    for aprendiz in aprendices:
        fichas.add(aprendiz["ficha"])

    for ficha in fichas:
        print("------------------------")
        print(f"Ficha: {ficha}")
        for aprendiz in aprendices:
            if aprendiz["ficha"] == ficha:
                print(f"Documento: {aprendiz['documento']}")
                print(f"Nombre: {aprendiz['nombre']}")
        print("------------------------")

def listar_evaluacion():
    """
    Esta función imprime en consola la lista de los aprendices agrupados por su estado de aprobación.
    """
    print("------------------------")
    print("Listado por calificaciones:")

    estados = {"Aprobado": [], "Desaprobado": []}

    # Clasificar los aprendices según su estado de evaluación
    for aprendiz in aprendices:
        estado = "Aprobado" if aprendiz["evaluacion"].lower() == 'a' else "Desaprobado"
        estados[estado].append(aprendiz)

    # Imprimir los aprendices aprobados
    print(f"{Fore.GREEN}Estado: Aprobado{Style.RESET_ALL}")
    for aprendiz in estados["Aprobado"]:
        print(f"Documento: {aprendiz['documento']}")
        print(f"Nombre: {aprendiz['nombre']}")
        print(f"Ficha: {aprendiz['ficha']}")
        print("------------------------")

    # Imprimir los aprendices desaprobados
    print(f"{Fore.RED}Estado: Desaprobado{Style.RESET_ALL}")
    for aprendiz in estados["Desaprobado"]:
        print(f"Documento: {aprendiz['documento']}")
        print(f"Nombre: {aprendiz['nombre']}")
        print(f"Ficha: {aprendiz['ficha']}")
        print("------------------------")

def borrar_usuario():
    """
    Esta función muestra los documentos y nombres antes de borrar un usuario.
    """
    # Mostrar todos los documentos con nombres
    print("------------------------")
    print("Documentos y nombres existentes:")
    for aprendiz in aprendices:
        print(f"Documento: {aprendiz['documento']}")
        print(f"Nombre: {aprendiz['nombre']}")
        print("------------------------")

    while True:
        documento = input("Ingrese el documento que desea borrar: ").lower()
        # Buscar el documento en la lista de aprendices
        for i, aprendiz in enumerate(aprendices):
            if aprendiz["documento"].lower() == documento:
                print("------------------------")
                print(f"Documento: {aprendiz['documento']}")
                print(f"Nombre: {aprendiz['nombre']}")
                print("------------------------")
                while True:
                    confirm = input("¿Está seguro que desea borrar este usuario? (si/no): ").lower()
                    if confirm == "si":
                        del aprendices[i]
                        print(f"Usuario con documento {documento} borrado.")
                        return
                    elif confirm == "no":
                        print("Borrado cancelado.")
                        return
                    else:
                        print("Por favor ingrese 'si' o 'no'.")
        else:
            print("Documento incorrecto. Por favor ingrese un número de documento existente.")



def listar_todos():
    """
    Esta función imprime en consola todos los aprendices registrados.
    """
    for aprendiz in aprendices:
            print("------------------------")
            print(f"Documento: {aprendiz["documento"]}")
            print(f"Nombre: {aprendiz['nombre']}")
            print(f"Evaluación: {aprendiz['evaluacion']}")
            print(f"Ficha: {aprendiz['ficha']}")
            print("------------------------")


def modificar_aprendiz():
    """
    Esta función muestra primero todos los documentos existentes y luego solicita al usuario que ingrese el documento del aprendiz que desea modificar.
    Permite al usuario decidir qué datos actualizar del aprendiz seleccionado.
    """
    # Mostrar todos los documentos existentes
    print("Documentos existentes:")
    for aprendiz in aprendices:
        print(f"Documento: {aprendiz['documento']}")

    documento = input("Ingrese el documento del aprendiz que desea modificar: ")
    
    # Buscar el documento en la lista de aprendices
    for i, aprendiz in enumerate(aprendices):
        if aprendiz["documento"] == documento:
            print("Ingrese los nuevos datos o presione Enter para mantener los actuales.")
            nuevo_nombre = input(f"Nombre actual: {aprendiz['nombre']}. Ingrese el nuevo nombre y apellidos: ")
            nueva_evaluacion = input(f"Evaluación actual: {aprendiz['evaluacion']}. Ingrese la nueva evaluación (A/D): ").lower()
            nueva_ficha = input(f"Ficha actual: {aprendiz['ficha']}. Ingrese la nueva ficha: ")

            # Actualizar solo los campos que el usuario decidió cambiar
            if nuevo_nombre:
                aprendices[i]['nombre'] = nuevo_nombre
            if nueva_evaluacion in ["a", "d"]:
                aprendices[i]['evaluacion'] = nueva_evaluacion.upper()
            if nueva_ficha:
                aprendices[i]['ficha'] = nueva_ficha

            print(f"Registro del aprendiz con documento {documento} actualizado exitosamente.")
            return
        else:
            print("No se encontró un aprendiz con ese documento. Por favor intente nuevamente.")


"""
En esta parte creamos el menu para poder digitar una de las opciones y segir el paso a paso para el usuario
"""

while True:
    print(F"{Fore.GREEN}\nMenu:{Fore.RESET}")
    print(Fore.LIGHTWHITE_EX + "1. Registro de aprendices")
    print("2. Lista de todos los aprendices")
    print("3. Listado por ficha")
    print("4. Listado por calificacion de evaluacion")
    print("5. Borrar usuario registrado")
    print("6. Lista de todos los datos registrados")
    print("7. Modificar aprendiz") 
    print("0. Salir" + Fore.RESET)

    opcion = input(F"{Fore.GREEN}Seleccione una opción: {Fore.RESET}")

    if opcion == "1":
        registrar_aprendiz()
    elif opcion == "2":
        listar_aprendices()
    elif opcion == "3":
        listar_ficha()
    elif opcion == "4":
        listar_evaluacion()
    elif opcion == "5":
        borrar_usuario()
    elif opcion == "6":
        listar_todos()
    elif opcion == "7":
        modificar_aprendiz() 
    elif opcion == "0":
        print("Proceso finalizado.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")