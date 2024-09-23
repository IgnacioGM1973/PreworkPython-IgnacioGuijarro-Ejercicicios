'''
Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo.
'''
from utilidades import controlar_repuesta_s_n, comprueba_numero_positivo

# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Calculadora de Área de un Rectángulo'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nPrograma que calcula el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.')
    print('\nEl usuario debe ingresar la longitud y el ancho del rectángulo.')


def comienza():
    respuesta = 's'
    area = 0
    base = 0
    altuta = 0
    while respuesta == 's':
        base = comprueba_numero_positivo("Introduzca la base en 'm': ")
        altura = comprueba_numero_positivo("Introduzca la altura en 'm': ")
        area = base * altura
        print(Fore.GREEN + '\n' + '*' * 70)
        print(f"El Área es de: {area} metro/s cuadrados")
        print('*' * 70 + Style.RESET_ALL)

        respuesta = controlar_repuesta_s_n()


def run():
    presentacion()
    comienza()
