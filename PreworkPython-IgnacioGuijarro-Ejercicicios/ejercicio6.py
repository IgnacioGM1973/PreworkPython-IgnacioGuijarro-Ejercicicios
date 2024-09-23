'''
Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''
from utilidades import comprueba_texto, controlar_repuesta_s_n

# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Verificación de Palíndromo'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nprograma que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda.')


def comienza():
    respuesta = 's'
    while respuesta == 's':
        texto = comprueba_texto("Introduzca una palabra: ")
        longitudTexto = len(texto)
        print(f"la longitud de texto es: {longitudTexto}")
        # print(texto[4:5])
        continicio = longitudTexto - 1
        contfin = longitudTexto
        texto2 = ""
        for i in range(longitudTexto):
            texto2 = texto2 + texto[continicio:contfin]
            continicio = continicio - 1
            contfin = contfin - 1
        if texto == texto2:
            print(Fore.GREEN + '\n' + '-' * 70)
            print(f'La palabra "{
                  texto}" es palíndromo".')
            print(Fore.GREEN + '-' * 70 + Style.RESET_ALL + '\n')
        else:
            print(Fore.RED + '\n' + '-' * 70)
            print(f'La palabra "{
                  texto}" NO ES palíndromo".')
            print(Fore.RED + '-' * 70 + Style.RESET_ALL + '\n')
        respuesta = controlar_repuesta_s_n()


def run():
    presentacion()
    comienza()
