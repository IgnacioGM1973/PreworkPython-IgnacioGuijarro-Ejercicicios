'''
Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.
'''
from utilidades import comprueba_numero_float, controlar_repuesta_s_n

# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Calculadora Simple'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nOperaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.')


def comienza():
    respuesta = 's'
    listaOpraciones = ('+', '-', '*', '/')
    numero1 = 0
    numero2 = 0
    resultado = 0
    while respuesta == 's':

        numero1 = comprueba_numero_float("Introduzca el primer número: ")
        while True:
            operacion = input("Operación: ")
            if operacion in listaOpraciones:
                break
            else:
                print(Fore.RED + '\n' + '*' * 70)
                print(f"Incorrecto, valores permitidos {listaOpraciones}")
                print('*' * 70 + Style.RESET_ALL)

        numero2 = comprueba_numero_float("Introduzca el segundo número: ")
        try:
            if operacion == '+':
                resultado = numero1 + numero2
            elif operacion == '-':
                resultado = numero1 - numero2
            elif operacion == '*':
                resultado = numero1 * numero2
            else:
                resultado = numero1 / numero2

            print(Fore.GREEN + '\n' + '*' * 70)
            print(f"EL resultado de {numero1} {
                  operacion} {numero2} = {resultado}")
            print('*' * 70 + Style.RESET_ALL)
        except ZeroDivisionError:
            print(f"Error. Los valores {numero1} y {
                numero2} no se puede dividir.")

        respuesta = controlar_repuesta_s_n()


def run():
    presentacion()
    comienza()


