# Lo importamos para ir limpiando la consola mientras el software se ejecuta
from os import system

import sys

# Lo importamos para crear y/o usar un archivo de texto donde se guardarán los usuarios
import json

class Iniciar_Sesion:

    def Obtener_Datos():
        print("INICIO DE SESIÓN")
        # Se obtienen los datos de entrada
        nombre = str(input("Por favor ingrese su nombre de usuario: "))
        contrasena = str(input("Por favor ingrese su contraseña: "))
        # Se limpia la consola para que todo se vea organizado
        system("cls")

        # Se llama al siguiente método para ingresar el usuario al programa   
        Iniciar_Sesion.Ingresar_Al_Software(nombre, contrasena)

        # Se llama nuevamente al método de Bienvenida para reiniciar el proceso
        return

    # Método donde se realizará todo el proceso de inicio de sesión
    def Ingresar_Al_Software(nombre, contrasena, archivo="usuarios.txt"):
        
        # Se validan que el usuario no haya dejado ningún dato sin llenar
        Iniciar_Sesion.validar_Valores_Vacios(nombre, contrasena)
        # Se valida que el usuario exista en el programa
        Iniciar_Sesion.validar_Existencia_Usuario(nombre)

        # Buscamos el usuario y la contraseña en el archivo .txt
        with open(archivo, "r") as file:
                for linea in file:
                    usuario = json.loads(linea.strip())
                    # Si el usuario y la contraseña son correctos, se ingresa el usuario al programa
                    if usuario.get("nombre") == nombre and usuario.get("contrasena") == contrasena:
                        print("Aún estamos en etapa de desarrollo, pero pronto tendremos más funcionalidades")
                        sys.exit()
        
        # Se lanza una excepción si la contraseña o el nombre de usuario son incorrectos
        raise Exception("ERROR: Nombre de usuario o Contraseña incorrectos")

    # Metodo para validar si hay algún valor vacío en lo que ingresa el usuario
    def validar_Valores_Vacios(nombre, contrasena):
        if nombre == "" or contrasena == "":
            raise Exception("ERROR: No pueden haber campos vacíos")

    # Método para validar que el usuario al que se le va a cambiar la contraseña exista
    def validar_Existencia_Usuario(nombre_buscado, archivo="usuarios.txt" ):
        with open(archivo, "r") as file:
            for linea in file:
                usuario = json.loads(linea.strip())
                if usuario.get("nombre") == nombre_buscado:
                    return
        raise Exception("ERROR: El usuario buscado no existe")

