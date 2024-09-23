'''
Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.
'''
from utilidades import controlar_repuesta_s_n, comprueba_numero_positivo_entero


# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Conversor de Tiempo'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nEscribe un programa que convierta un número de minutos en horas y minutos. ')
    print('\nPor ejemplo, 145 minutos serían 2 horas y 25 minutos.')


def convertir_minutos(minutos):
    horas = minutos // 60  # División entera para obtener las horas
    minutos_restantes = minutos % 60  # El resto serán los minutos restantes
    return horas, minutos_restantes


def comienza():
    respuesta = 's'
    resultado = 0

    while respuesta == 's':
        print(Fore.YELLOW + '\n' + '*' * 70)
        minutos = comprueba_numero_positivo_entero("Introduzca numero: ")
        print('*' * 70 + Style.RESET_ALL)

        horas, minutos_restantes = convertir_minutos(minutos)

        print(Fore.GREEN + '\n' + '*' * 70)
        print(f"{minutos} minutos son {horas} horas y {
              minutos_restantes} minutos.")
        print('*' * 70 + Style.RESET_ALL)

        respuesta = controlar_repuesta_s_n()


def run():
    presentacion()
    comienza()
