'''
Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.
'''
from utilidades import controlar_repuesta_s_n, comprueba_numero_float

# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Ejercicio 14: Calculadora de Descuento'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nPrograma que calcula el precio final de un artículo después de aplicar un descuento del 20%.')


def comienza():
    respuesta = 's'
    resultado = 0

    while respuesta == 's':
        print(Fore.YELLOW + '\n' + '*' * 70)
        n = comprueba_numero_float("Introduzca el precio del artículo: ")
        print('*' * 70 + Style.RESET_ALL)
        resultado = n - (n * 0.20)  # calular el descuento
        print(Fore.GREEN + '\n' + '*' * 70)
        print(f"El  precio del artículo despues de aplicar el 20% es de: {
              resultado} €.")
        print('*' * 70 + Style.RESET_ALL)

        respuesta = controlar_repuesta_s_n()


def run():
    presentacion()
    comienza()
