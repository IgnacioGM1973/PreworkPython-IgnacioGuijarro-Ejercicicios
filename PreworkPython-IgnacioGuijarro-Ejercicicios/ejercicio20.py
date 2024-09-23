'''
Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario.
'''
from utilidades import controlar_repuesta_s_n, comprueba_numero_float


# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Suma de Números en una Lista'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nPrograma que suma todos los números en una lista ingresada por el usuario.')


def sumar_lista(lista):
    print(Fore.GREEN + '\n' + '*' * 70)
    print(f"La suma de los números de la lista es: {sum(lista)}")
    print('*' * 70 + Style.RESET_ALL)


def comienza():
    lista = []
    respuesta = 's'

    while respuesta == 's':
        print(Fore.YELLOW + '\n' + '*' * 70)
        lista.append(comprueba_numero_float("Introduzca un número: "))
        print(Fore.YELLOW + '*' * 70 + Style.RESET_ALL)
        respuesta = controlar_repuesta_s_n()
    sumar_lista(lista)


def run():
    presentacion()
    comienza()
