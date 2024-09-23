'''
Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.
'''
from utilidades import controlar_repuesta_s_n, comprueba_numero_positivo_float


# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Contador de Palabras'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nCrea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.')


def contadorPalabras(oracion):

    oracion = oracion.replace(".", " ")
    oracion = oracion.replace("'", " ")
    oracion = oracion.replace('"', " ")
    oracion = oracion.replace(',', " ")
    texto = oracion.split(" ")
    texto = [i for i in texto if i != ""]
    print(Fore.GREEN + '\n' + '*' * 70)
    print(f"El número de palabras es {len(texto)}")
    print('*' * 70 + Style.RESET_ALL)


def comienza():
    respuesta = 's'
    lista = []

    while respuesta == 's':
        respuesta = 's'
        print(Fore.YELLOW + '\n' + '*' * 70)
        oracion = input("Introduzca una oración: ")
        contadorPalabras(oracion)

        respuesta = controlar_repuesta_s_n()


def run():
    presentacion()
    comienza()
