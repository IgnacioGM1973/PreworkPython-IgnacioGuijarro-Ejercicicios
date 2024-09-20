'''
Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no
'''
from utilidades import controlar_repuesta_s_n

# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Verificación edad'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nEste programa solicita la edad de un usuario y determine si es mayor de edad (mayor o igual a 18 años) o no.,')


def chequeaEdad(edad):
    if edad >= 18:
        print(Fore.GREEN + '\n' + '*' * 29)
        print("***** Eres mayor de edad ****")
        print("*" * 29)
    else:
        print(Fore.RED + '\n' + '*' * 29)
        print("***** Eres menor de edad ****")
        print("*" * 29)
    print(Style.RESET_ALL)
    print('-' * 29 + Style.RESET_ALL)


def comienza():
    respuesta = 's'
    while respuesta == 's':
        try:
            edad = int(input("Introduce la edad: "))
            chequeaEdad(edad)
            respuesta = controlar_repuesta_s_n()

        except ValueError:
            print("El dato tiene que ser númerico, intentelo otra vez.")


def run():
    presentacion()
    comienza()
