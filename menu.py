import sys

import pyperclip

from cliente_servidor import opcioneswebsocket
from desencriptar import desencriptar
from encriptar import encriptar


def menu_principal():
    menu1 = {
        "1": encriptar_texto,
        "2": desencriptar_texto,
        "3": iniciarconversacion,
        "4": menu_de_salida,
    }
    texto_menu = (
        "\n1 = encriptar\n2 = desencriptar\n3 = iniciar una conversacio\n4 = exit"
    )
    var = input(f"Bienvenido al menu de opciones {texto_menu}\n")
    while var != "1" and var != "2" and var != "3" and var != "4":
        var = input(f"Opcion no valida, intente de nuevo\n")
    print(f"escogiste la opcion {var}")
    menu1.get(var)()


def menu_de_salida():
    if input("Confirmar que quieres salir\n").upper() == "SI":
        sys.exit("Gracias por usar el programa")
    else:
        if input("Entoces quieres volver al menu?\n").upper() == "SI":
            menu_principal()
        else:
            menu_de_salida()


def desencriptar_texto():
    try:
        texto_a_descifrar = input("Introduce el mensaje encriptado: ")
        desencriptar(texto_a_descifrar)
        if input("Quieres volver al menu principal?: ").upper() == "SI":
            menu_principal()
        else:
            menu_de_salida()
    except ValueError:
        print("Lo siento no se puedo decifrar el mensaje")
        desencriptar_texto()


def encriptar_texto():
    try:
        texto_a_descifrar = encriptar()
        pyperclip.copy(texto_a_descifrar)
        print("El mensaje encriptado fue copiado para ser usado luego")
        if input("Quieres desencriptar el mensaje: ") == "si":
            desencriptar(texto_a_descifrar)
            if input("Quieres volver al menu principal?: ").upper() == "SI":
                menu_principal()
            else:
                menu_de_salida()
        else:
            menu_de_salida()
    except KeyError:
        print("Lo siento no se puedo encriptar el mensaje")
        encriptar_texto()


def iniciarconversacion():
    opcioneswebsocket()


menu_principal()
