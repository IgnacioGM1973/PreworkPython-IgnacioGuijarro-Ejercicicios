# Funciones globales

try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color

# Controla respuesta (s/n)
def controlar_repuesta_s_n():
    while True:
        respuesta = input("¿Desea continuar añadiendo valores? (s/n): ")
        if respuesta.lower() in ['s', 'n']:
            return respuesta.lower()
        else:
            print(Fore.RED + '\n' + '*' * 70)
            print("Por favor, responda con 's' para sí o 'n' para no.")
            print('*' * 70 + Style.RESET_ALL)


def menu():
    print("---------------------------------------------------------")
    print("*    Ejercicios Introducción a Python: Enunciados       *")
    print("---------------------------------------------------------")
    print("Ejercicio 1: Conversor de Temperatura")
    print("Ejercicio 2: Calculadora de Propina")
    print("Ejercicio 3: Verificación de Edad")
    print("Ejercicio 4: Contador de Vocales")
    print("Ejercicio 5: Suma de Números Pares")
    print("Ejercicio 6: Verificación de Palínd")
    print("Ejercicio 7: Calculadora Simple")
    print("Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)")
    print("Ejercicio 9: Conversor de Divisas")
    print("Ejercicio 10: Determinar el Día de la Semana")
    print("Ejercicio 11: Calculadora de Edad")
    print("Ejercicio 12: Calculadora de Área de un Rectángulo")
    print("Ejercicio 13: Verificación de Número Primo")
    print("Ejercicio 14: Calculadora de Descuento")
    print("Ejercicio 15: Conversor de Tiempo")
    print("Ejercicio 16: Contador de Números Pares e Impares")
    print("Ejercicio 17: Conversor de Millas a Kilómetros")
    print("Ejercicio 18: Contador de Palabras")
    print("Ejercicio 19: Verificación de Año Bisiesto")
    print("Ejercicio 20: Suma de Números en una Lista")
    print("---------------------------------------------------------")


def comprueba_texto(texto):
    '''
    Función que valida si es solo texto lo introducido.
    De lo contrario da error.
    Ejemplo:
    varTexto = comprueba_texto("Introduce un texto: ")
    '''
    while True:
        textoAcomprobar = ""
        textoAcomprobar = input(texto)

        if textoAcomprobar.isalpha():
            print("texto correcto")
            return textoAcomprobar
        else:
            print(Fore.RED + '\n' + '*' * 70)
            print("Tiene que ser texto. Intentelo otra vez.")
            print('*' * 70 + Style.RESET_ALL)


def comprueba_numero_entero(texto):
    '''
    Función que valida que lo intrucido sea solo un número entero.
    De lo contrario da error.
    Ejemplo:
    varTexto = comprueba_texto("Introduce un número entero: ")
    '''
    while True:
        try:
            print("-" * 70)
            numero = int(input(texto))
            print("-" * 70)
            return numero
        except ValueError:
            print(Fore.RED + '\n' + '*' * 70)
            print("Error, Tiene que ser un número entero.")
            print('*' * 70 + Style.RESET_ALL)


def comprueba_numero_float(texto):
    '''
    Función que valida que lo intrucido sea solo un número entero.
    De lo contrario da error.
    Ejemplo:
    varTexto = comprueba_texto("Introduce un número entero: ")
    '''
    while True:
        try:
            print("-" * 70)
            numero = float(input(texto))
            print("-" * 70)
            return numero
        except ValueError:
            print(Fore.RED + '\n' + '*' * 70)
            print("Error, Tiene que ser un número.")
            print('*' * 70 + Style.RESET_ALL)
def comprueba_numero_positivo_float(texto):
    '''
    Función que valida que lo intrucido sea solo un número entero positivo y entero.
    De lo contrario da error.
    '''
    valor = True
    while valor == True:
        try:
            print("-" * 70)
            numero = float(input(texto))
            print("-" * 70)
            if numero >= 1:
                return numero
            else:
                print(Fore.RED + '\n' + '*' * 70)
                print("Error, Tiene que ser un número postivo y mayor de 0.")
                print('*' * 70 + Style.RESET_ALL)
                valor = True
        except ValueError:
            print(Fore.RED + '\n' + '*' * 70)
            print("Error, Tiene que ser un número.")
            print('*' * 70 + Style.RESET_ALL)

            
def comprueba_numero_positivo(texto):
    '''
    Función que valida que lo intrucido sea solo un número entero positivo.
    De lo contrario da error.
    '''
    valor = True
    while valor == True:
        try:
            print("-" * 70)
            numero = float(input(texto))
            print("-" * 70)
            if numero >= 1:
                return numero
            else:
                print(Fore.RED + '\n' + '*' * 70)
                print("Error, Tiene que ser un número postivo y mayor de 0.")
                print('*' * 70 + Style.RESET_ALL)
                valor = True
        except ValueError:
            print(Fore.RED + '\n' + '*' * 70)
            print("Error, Tiene que ser un número.")
            print('*' * 70 + Style.RESET_ALL)

def comprueba_numero_positivo_entero(texto):
    '''
    Función que valida que lo intrucido sea solo un número entero positivo y entero.
    De lo contrario da error.
    '''
    valor = True
    while valor == True:
        try:
            print("-" * 70)
            numero = int(input(texto))
            print("-" * 70)
            if numero >= 1:
                return numero
            else:
                print(Fore.RED + '\n' + '*' * 70)
                print("Error, Tiene que ser un número postivo y mayor de 0.")
                print('*' * 70 + Style.RESET_ALL)
                valor = True
        except ValueError:
            print(Fore.RED + '\n' + '*' * 70)
            print("Error, Tiene que ser un número.")
            print('*' * 70 + Style.RESET_ALL)

