'''
 Ejercicio 1: Conversor de Temperatura
 Escribe un programa que convierta una temperatura de grados Celsius a grados 
 Fahrenheit.
'''
# Incorporo función ya creada

from utilidades import controlar_repuesta_s_n, comprueba_numero_float

# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color



def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Conversor de Temperatura'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nPrograma que convierta una temperatura de grados Celsius a grados Fahrenheit.')
    


def gCelsius(celsius):
    Fahrenheit = (float(celsius) * 1.8) + 32
    print(Fore.GREEN + '\n' + '*' * 70)
    print(f"El resultado es: {Fahrenheit:.2f} grados Fahrenheit")
    print('*' * 70 + Style.RESET_ALL)


def comienza():
    respuesta = 's'
    celsius = 0
    while respuesta == 's':
        try:
            print(Fore.YELLOW + '\n' + '*' * 70)
            celsius = comprueba_numero_float("Celsius: ")
            print('*' * 70 + Style.RESET_ALL)
            gCelsius(celsius)
            respuesta = controlar_repuesta_s_n()
            

        except ValueError:
            print(Fore.RED + '\n' + '*' * 70)
            print("El dato tiene que ser númerico, intentelo otra vez.")
            print('*' * 70 + Style.RESET_ALL)


def run():
    presentacion()
    comienza()
