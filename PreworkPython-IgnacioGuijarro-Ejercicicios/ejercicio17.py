'''
Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros.
'''
from utilidades import controlar_repuesta_s_n, comprueba_numero_positivo_float


# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Conversor de Millas a Kilómetros'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nEscribe un programa que convierta una distancia en millas a kilómetros.')
    print('\nSabiendo que 1 milla equivale a 1.60934 kilómetros. ')


def convertir_km_a_millas(millas):
    kilometros = millas * 1.60934
    print(Fore.GREEN + '\n' + '*' * 70)
    print(f"{millas} millas son {kilometros:.2f} kilometros.")
    print('*' * 70 + Style.RESET_ALL)


def comienza():
    respuesta = 's'
    lista = []

    while respuesta == 's':
        respuesta = 's'
        print(Fore.YELLOW + '\n' + '*' * 70)
        millas = comprueba_numero_positivo_float("Introduzca numero de Millas: ")
        print('*' * 70 + Style.RESET_ALL)
        convertir_km_a_millas(millas)

        respuesta = controlar_repuesta_s_n()


def run():
    presentacion()
    comienza()


