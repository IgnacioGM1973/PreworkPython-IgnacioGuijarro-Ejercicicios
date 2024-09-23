'''
Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no.
'''
from utilidades import controlar_repuesta_s_n, comprueba_numero_float

# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Ejercicio 13: Verificación de Número Primo'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nPrograma que determina si un número ingresado por el usuario es primo no.')


def comienza():
    respuesta = 's'
    numero = 0

    while respuesta == 's':

        n = comprueba_numero_float("Introduzca un número positivo: ")
        if n < 1:
            print(Fore.RED + '\n' + '*' * 70)
            print(f"El  número  {n} no es primo.")
            print('*' * 70 + Style.RESET_ALL)
        else:
            sw = 0
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    sw = 1
            if sw == 0:
                print(Fore.GREEN + '\n' + '*' * 70)
                print(f"El  número  {n} es primo.")
                print('*' * 70 + Style.RESET_ALL)
            else:
                print(Fore.RED + '\n' + '*' * 70)
                print(f"El  número  {n} No es primo.")
                print('*' * 70 + Style.RESET_ALL)

        respuesta = controlar_repuesta_s_n()


def run():
    presentacion()
    comienza()
