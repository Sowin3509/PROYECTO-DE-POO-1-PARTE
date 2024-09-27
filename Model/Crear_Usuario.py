# Lo importamos para ir limpiando la consola mientras el programa se ejecuta
from os import system

# Lo importamos para crear y/o usar un archivo de texto donde se guardarán los usuarios
import json


class Crear_Usuario:

    # Metodo para crear el usuario con sus parametros
    def Generar_Usuario():
        print("DATOS PERSONALES")
        # Se obtienen los datos de entrada
        nombre = str(input("Por favor ingrese su nombre de usuario: "))
        contrasena = str(input("Por favor ingrese su contraseña: "))
        # Se limpia la consola para que todo se vea organizado
        system("cls")

        # Se validan que el usuario no haya dejado ningun dato sin llenar
        Crear_Usuario.validar_Valores_Vacios(nombre, contrasena)
        # Se valida que no exista ningun usuario con ese nombre
        Crear_Usuario.validar_Existencia_Usuario(nombre)

        # Se crea el usuario con los datos que ingresó
        usuario = {"nombre": nombre,
                "contrasena": contrasena}

        # Se llama al siguiente metodo para guardar al usuario en el archivo .txt        
        Crear_Usuario.Guardar_Usuario(usuario)

        # Se llama nuevamente al metodo de Bienvenida para reiniciar el proceso
        return
        
    # Metodo donde se realizará todo el proceso de registro
    def Guardar_Usuario(usuario, archivo="usuarios.txt"):   
        # Se utilizan los metodos de la libreria "Json" para acceder al archivo de texto y guardar el usuario allí
        with open(archivo, "a") as file:
            file.write(json.dumps(usuario) + "\n")

        # Se muestra un mensaje indicando que todo salió bien
        print("USUARIO CREADO EXITOSAMENTE")

        # Se retorna al metodo anterior que invoco este metodo
        return
    
    # Metodo para validar si hay algun valor vacio en lo que ingresa el usuario
    def validar_Valores_Vacios(nombre, contrasena):
        if nombre == "" or contrasena == "":
            raise Exception("ERROR: No pueden haber campos vacios")
    
    # Metodo para validar que no exista ningun usuario ya creado con ese nombre
    def validar_Existencia_Usuario(nombre_buscado, archivo="usuarios.txt" ):
        with open(archivo, "r") as file:
            for linea in file:
                usuario = json.loads(linea.strip())
                if usuario.get("nombre") == nombre_buscado:
                    raise Exception("ERROR: Ya existe un usuario con ese nombre")



