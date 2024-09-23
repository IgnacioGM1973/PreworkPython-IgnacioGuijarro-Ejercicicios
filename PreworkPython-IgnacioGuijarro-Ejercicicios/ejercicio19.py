'''
Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.
'''
from utilidades import controlar_repuesta_s_n, comprueba_numero_positivo_entero


# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Verificación de Año Bisiesto'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nPrograma que determine si un año ingresado por el usuario es bisiesto o no.')


def comprobar_año_bisiesto(año):

    
    if (año % 4 == 0 and año % 100 !=0) or (año % 400 ==0):
        print(Fore.GREEN + '\n' + '*' * 70)
        print("El año es bisiesto")
        print('*' * 70 + Style.RESET_ALL)
    else:
        print(Fore.MAGENTA + '\n' + '*' * 70)
        print("El año no es bisiesto")
        print('*' * 70 + Style.RESET_ALL)


def comienza():
    respuesta = 's'
    lista = []

    while respuesta == 's':
        respuesta = 's'
        print(Fore.YELLOW + '\n' + '*' * 70)
        comprobar_año_bisiesto(
            comprueba_numero_positivo_entero("Introduzca un año: "))
        print(Fore.YELLOW + '*' * 70 + Style.RESET_ALL)
        respuesta = controlar_repuesta_s_n()


def run():
    presentacion()
    comienza()


