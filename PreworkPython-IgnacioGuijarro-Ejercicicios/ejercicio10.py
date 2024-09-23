'''
Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc).
'''
from utilidades import comprueba_numero_entero, controlar_repuesta_s_n

# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Determinar el Día de la Semana'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nEscribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.)')


def comienza():
    respuesta = 's'
    listaDiasSemana = ('lunes','martes','miercoles','jueves','viernes','sabado','domingo',1,2,3,4,5,6,7)
    
    while respuesta == 's':
        while True:
            numero1 = comprueba_numero_entero("Introduzca el número de la semana: ")
            if numero1 in listaDiasSemana:
              print(Fore.GREEN + '\n' + '*' * 70)
              print(f"El día de la semana según el número introducido {numero1} es: {listaDiasSemana[numero1-1]}")
              print('*' * 70 + Style.RESET_ALL)
              break
            else:
              print(Fore.RED + '\n' + '*' * 70)
              print(f"El número {numero1} no es correcto, el valor tiene que ser entre 1 y 7.")
              print('*' * 70 + Style.RESET_ALL)
              
        
        respuesta = controlar_repuesta_s_n()


def run():
    presentacion()
    comienza()
