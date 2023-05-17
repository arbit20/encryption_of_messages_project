from biblioteca import code_base


# from messenger import messengertodecifrar


def encriptar():
    message_to_encrypted = messengertodecifrar()
    text_save = ""
    for index in message_to_encrypted:
        encryption_codes_inverted = code_base[index]
        text_save = text_save + encryption_codes_inverted
    result = show_encrypted_message(text_save)
    print(f"Message successfully encrypted: {result}")
    return text_save


def messengertodecifrar():
    message = input("Type a message to encrypt: ")
    return message


def show_encrypted_message(text_to_display):
    text_save = ""
    for element in text_to_display:
        text_save += element
    return text_save
