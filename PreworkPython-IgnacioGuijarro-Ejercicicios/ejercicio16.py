'''
Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario
'''
from utilidades import controlar_repuesta_s_n, comprueba_numero_positivo_entero


# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Conversor de Tiempo'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nPrograma que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario ')


def n_pares(lista):

    listaPares = []
    listaImpares = []

    for i in lista:
        if i % 2 == 0:
            listaPares.append(i)
        else:
            listaImpares.append(i)

    print(Fore.GREEN + '\n' + '*' * 70)
    print(f"Numeros pares: {listaPares}")
    print(f"Cantidad de números pares: {len(listaPares)}")
    print(f"La suma de los numeros pares es: {sum(listaPares)}")
    print('*' * 70 + Style.RESET_ALL)

    print(Fore.CYAN + '\n' + '*' * 70)
    print(f"Numeros impares: {listaImpares}")
    print(f"Cantidad de números impares: {len(listaImpares)}")
    print(f"La suma de los numeros impares es: {sum(listaImpares)}")
    print('*' * 70 + Style.RESET_ALL)


def comienza():
    respuesta = 's'
    lista = []

    while respuesta == 's':
        respuesta = 's'
        print(Fore.YELLOW + '\n' + '*' * 70)
        lista.append(comprueba_numero_positivo_entero("Introduzca numero: "))
        print('*' * 70 + Style.RESET_ALL)
        respuesta = controlar_repuesta_s_n()

    n_pares(lista)


def run():
    presentacion()
    comienza()


