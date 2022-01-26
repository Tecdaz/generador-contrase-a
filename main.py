from random import choice
import pyperclip


def generator(characters, length):
    password = []
# selecciona un caracter random de la lista de caracteres que escogio el usuario
    for i in range(length):
        password += choice(characters)
    
    return "".join(password)


def run():
    print("Generador random de contraseña.\n")
# Listas con caracteres que puede contener una contraseña
    minus = list("abcdefghijklmnñopqrstuvwxyz")
    mayus = [letter.upper() for letter in minus]
    numbers = list("1234567890")
    symbols = list(" !\"#$%&'()*+,-./:;<=>?@][^_`{|}~")
# Por default agrega siempre minusculas 
    character_list = minus

    options = ["mayusculas", "numeros", "simbolos"]

    for index, option in enumerate(options):
        answer = input(f"Desea agregar {option}? (s/n): ")
# Depende del orden que den si, se concatena una lista
        if (answer == "s") or (answer == "S"):
            if index == 0:
                character_list += mayus
            elif index == 1:
                character_list += numbers
            else:
                character_list += symbols
    
    length = int(input("Cual es el largo de la cotraseña?: "))
    password = generator(character_list, length)
# Copia la contraseña al portapapeles
    pyperclip.copy(password)
    print(password)


if __name__ == '__main__':
    run()