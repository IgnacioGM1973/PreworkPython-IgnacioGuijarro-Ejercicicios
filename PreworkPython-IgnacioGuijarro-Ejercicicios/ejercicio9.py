'''
Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.
'''
from utilidades import comprueba_numero_float, controlar_repuesta_s_n

# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Conversor de Divisas'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nPrograma que convierte una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.')


def comienza():
    respuesta = 's'
    numero1 = 0
    resultado = 0
    while respuesta == 's':

        numero1 = comprueba_numero_float(
            "Introduzca cantidad de dolares a convertir: ")
        try:
            if numero1 < 1:
                print(Fore.RED + '\n' + '*' * 70)
                print(
                    "Error , los datos introducidos no son correctos! No pueden ser ni negativos ni 0.")
                print('*' * 70 + Style.RESET_ALL)
            else:
                resultado = numero1 * 0.85
                print(Fore.GREEN + '\n' + '*' * 70)
                print(F"Euros = {resultado}€")
                print('*' * 70 + Style.RESET_ALL)

        except ZeroDivisionError:
            print(Fore.RED + '\n' + '*' * 70)
            print(
                "Error , los datos introducidos no son correctos! ")
            print('*' * 70 + Style.RESET_ALL)
        respuesta = controlar_repuesta_s_n()


def run():
    presentacion()
    comienza()
