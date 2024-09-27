# Lo importamos para ir limpiando la consola mientras el programa se ejecuta
from os import system

# Lo importamos para terminar la ejecución del programa cuando el usuario quera salir
import sys

# Se importa el modulo donde se realizarán los procesos
from Model.Crear_Usuario import Crear_Usuario
from Model.Cambiar_Contrasena import Cambiar_Contrasena
from Model.Iniciar_Sesion import Iniciar_Sesion

# Se le da una bienvenida al usuario y se le muestra un menú con las opciones
def Inicio():
    print("")
    print("BIENVENIDO A TU RED SOCIAL, ¿QUE DESEAS HACER?")
    print("")
    print("0.Salir, 1.Iniciar Sesión, 2.Crear una Cuenta, 3.Cambiar Contraseña")
    opcion = int(input("Elija una opción: "))
    print("")

    # Se llama a la siguiente función y se le pasa como parámetro la opción que el usuario eligió
    eleccion(opcion)

def eleccion(opcion):
    # Se hace uso del método try para lanzar una excepción si algo falla
    try:
        # Se verifica si la opción escogida por el usuario no está definida
        if opcion < 0 or opcion > 3:
            system("cls")
            print("La opción ingresada no es correcta, intente de nuevo")
            # Se llama nuevamente al método de Bienvenida para reiniciar el proceso
            Inicio()
        
        if opcion == 0:
            # Se limpia la consola para que todo se vea organizado
            system("cls")
            # Se le da al usuario un mensaje de despedida al usuario cuando finaliza todo el proceso
            print("Aquí te esperaremos nuevamente ")
            # Se termina el programa
            sys.exit()

        # Se verifica si el usuario quiere iniciar sesión en el programa
        if opcion == 1:
            # Se limpia la consola para que todo se vea organizado
            system("cls")
            # Se llama la función "Obtener_Datos" para llevar al usuario hasta allí
            Iniciar_Sesion.Obtener_Datos()
            
        # Se verifica si el usuario quiere crear una cuenta en el programa
        if opcion == 2:
            # Se limpia la consola para que todo se vea organizado
            system("cls")
            
            # Se llama la función "Generar_Usuario" para llevar al usuario hasta allí
            Crear_Usuario.Generar_Usuario()
            # Se llama nuevamente al método de Bienvenida para reiniciar el proceso
            Inicio()

        # Se verifica si el usuario quiere cambiar la contraseña de su cuenta
        if opcion == 3:
            # Se limpia la consola para que todo se vea organizado
            system("cls")
            
            # Se llama la función "Obtener_Datos" para llevar al usuario hasta allí
            Cambiar_Contrasena.Obtener_Datos()
            # Se llama nuevamente al método de Bienvenida para reiniciar el proceso
            Inicio()

    # Se lanza un mensaje de error cuando algo falla
    except Exception as exc:
        # Se limpia la consola para que todo se vea organizado
        system("cls")
        print(f"{exc}, intentalo nuevamente")
        print("-------------------------------------------------------------------------")
        print("")
        # Se llama nuevamente al método de Bienvenida para reiniciar el proceso
        Inicio()

# Llamado que se hace por primera vez cuando se ejecuta el programa
Inicio()

