from biblioteca import code_base


def dividir_string(cadena):
    resultado = []
    for i in range(0, len(cadena), 5):
        resultado.append(cadena[i:i + 5])
    return resultado


def devolver_key(valor):
    final = list(code_base.keys())[list(code_base.values()).index(valor)]
    return final


def desencriptar(texto):
    texto_final = ""
    lista_dividida = dividir_string(texto)
    for element in lista_dividida:
        reemplazo = devolver_key(element)
        texto_final = texto_final + reemplazo
    a = show_encrypted_message1(texto_final)
    print(f"Mensaje desencriptado con exito: {a}")
    return texto_final


def show_encrypted_message1(text_to_display):
    decrypted_message_to_display = ""
    for elements_of_the_message in text_to_display:
        decrypted_message_to_display += elements_of_the_message
    return decrypted_message_to_display
