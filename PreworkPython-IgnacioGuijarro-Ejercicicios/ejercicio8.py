'''
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''
from utilidades import comprueba_numero_float, controlar_repuesta_s_n

# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Cálculo del Índice de Masa Corporal (IMC)'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nPrograma que calcula el Índice de Masa Corporal (IMC) de una persona.')


def comienza():
    respuesta = 's'
    numero1 = 0
    numero2 = 0
    resultado = 0
    while respuesta == 's':

        numero1 = comprueba_numero_float("Introduzca el peso: ")
        numero2 = comprueba_numero_float("Introduzca la altura: ")

        try:
            resultado = numero1 / (numero2 ** 2)
            print(Fore.GREEN + '\n' + '*' * 70)
            print(f"EL IMC ES DE: {resultado:.2f}")
            print('*' * 70 + Style.RESET_ALL)

        except ZeroDivisionError:
            print(Fore.RED + '\n' + '*' * 70)
            print(
                "No se puede calcular el IMC, los datos introducidos no son correctos! ")
            print('*' * 70 + Style.RESET_ALL)
        respuesta = controlar_repuesta_s_n()


def run():
    presentacion()
    comienza()


