'''
Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.
'''

from utilidades import controlar_repuesta_s_n, comprueba_texto

# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Contador de vocales'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nPrograma que cuenta el número de vocales en una palabra ingresada por el usuario.,')


def chequeaTexto(edad):
    pass


def es_texto():
    vocales = ["a", "e", "i", "o", "u"]
    contaVocal = 0
    while True:
        print("*" * 70)
        texto = input("Ingresa un texto: ")
        print("*" * 70)
        cadenaSoloTexto = texto.isalpha()
        if cadenaSoloTexto:
            print("¡Es un texto válido!")
            for i in texto:
                if i.lower() in vocales:
                    contaVocal += 1
            print("*" * 70)
            print(Fore.BLUE, 'El número de vocales que tiene la palabra "',
                  texto, '" es de ', Fore.GREEN,  contaVocal, Style.RESET_ALL)
            print("*" * 70)
            break
        else:
            print("-" * 70)
            print(
                Fore.RED + "No puede haber números en la palabra. Inténtalo de nuevo." + Style.RESET_ALL)
            print("-" * 70)


def comienza():
    respuesta = 's'
    while respuesta == 's':
        try:
            es_texto()
            '''
            texto = input("introduce el texto ")
            cadena = texto.isalpha()
            print(cadena)
            '''
            respuesta = controlar_repuesta_s_n()

        except ValueError:
            print("El dato tiene que ser texto, intentelo otra vez.")


def run():
    presentacion()
    comienza()
