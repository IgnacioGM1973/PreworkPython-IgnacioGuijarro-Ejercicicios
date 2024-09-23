'''
Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.
'''
from utilidades import comprueba_numero_entero, controlar_repuesta_s_n
from datetime import datetime

# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Calculadora de Edad'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nEscribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.')


def comienza():
    respuesta = 's'
    
    while respuesta == 's':
        año = False
        añoActual = datetime.now().year
        print(Fore.BLUE + '\n' + '*' * 70)
        print(f"              El año actual es {añoActual}.")
        print('*' * 70 + Style.RESET_ALL)
        
        while año == False:
            numero1 = comprueba_numero_entero("Introduzca el año de nacimiento: ")
            edad = añoActual - numero1
            if numero1 >= 0:
              año = True
              print(Fore.GREEN + '\n' + '*' * 70)
              print(f"Tu edad según tu año de nacimiento {numero1}, en el {añoActual} es o será de: {edad}")
              print('*' * 70 + Style.RESET_ALL)
              break
            else:
              print(Fore.RED + '\n' + '*' * 70)
              print(f"El número {numero1} no es correcto, el valor no puede ser menor de 0.")
              print('*' * 70 + Style.RESET_ALL)
              
        
        respuesta = controlar_repuesta_s_n()


def run():
    presentacion()
    comienza()

