# Lo importamos para ir limpiando la consola mientras el software se ejecuta
from os import system

# Lo importamos para crear y/o usar un archivo de texto donde se guardarán los usuarios
import json

class Cambiar_Contrasena:

    def Obtener_Datos():
        print("CAMBIO DE CONTRASEÑA")
        # Se obtienen los datos de entrada
        nombre = str(input("Por favor ingrese su nombre de usuario: "))
        nueva_contrasena = str(input("Por favor ingrese su nueva contraseña: "))
        # Se limpia la consola para que todo se vea organizado
        system("cls")

        # Se llama al siguiente método para cambiar la contraseña del usuario en el archivo .txt   
        Cambiar_Contrasena.Asignar_Nueva_Contrasena(nombre, nueva_contrasena)

        # Se llama nuevamente al método de Bienvenida para reiniciar el proceso
        return

    # Método donde se realizará todo el proceso de cambio de contraseña
    def Asignar_Nueva_Contrasena(nombre, nueva_contrasena, archivo="usuarios.txt"):
        
        # Se validan que el usuario no haya dejado ningún dato sin llenar
        Cambiar_Contrasena.validar_Valores_Vacios(nombre, nueva_contrasena)
        # Se valida que el usuario exista en el programa
        Cambiar_Contrasena.validar_Existencia_Usuario(nombre)

        #Se crea una lista donde se guardará el usuario con la contraseña nueva y todos los demás usuarios seguirán iguales
        usuario_cambiado = []
        #Se obtiene cada usuario del archivo
        with open(archivo, "r") as file:
            for linea in file:
                usuario = json.loads(linea.strip())
                # Si el usuario que encontramos en el archivo es el que estamos buscando, se le cambia la contraseña
                if usuario.get("nombre") == nombre:
                    usuario["contrasena"] = nueva_contrasena
                usuario_cambiado.append(usuario)
        
        # Se vuelven a cargar todos los usuarios al archivo .txt
        with open(archivo, "w") as file:
            for usuario in usuario_cambiado:
                file.write(json.dumps(usuario) + "\n")

        # Se retorna al método anterior que invoco este método
        return
    

    # Método para validar si hay algún valor vacío en lo que ingresa el usuario
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

