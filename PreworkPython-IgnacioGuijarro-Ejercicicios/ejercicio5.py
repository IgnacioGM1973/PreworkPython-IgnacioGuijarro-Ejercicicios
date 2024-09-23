'''
Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
'''
from utilidades import comprueba_numero_entero, controlar_repuesta_s_n

# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Calcular la suma de todos los números pares del 1 al 100'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nPrograma que calcula la suma de todos los números pares del 1 al 100.')


def comienza():
    respuesta = 's'
    while respuesta == 's':
        lista_numeros = []
        numero = comprueba_numero_entero("\nIntroduzca un número: ")
        for i in range(1, numero + 1):
            if i % 2 == 0:
                lista_numeros.append(i)
        total = sum(lista_numeros)
        print(Fore.GREEN + '\n' + '-' * 70)
        print(f"El total de la suma de los números pares del 1 al {
              numero} es : {total}")
        print(Fore.GREEN + '-' * 70 + Style.RESET_ALL + '\n')
        respuesta = controlar_repuesta_s_n()


def run():
    presentacion()
    comienza()
