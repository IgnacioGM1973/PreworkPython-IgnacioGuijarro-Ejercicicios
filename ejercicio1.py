'''
 Ejercicio 1: Conversor de Temperatura
 Escribe un programa que convierta una temperatura de grados Celsius a grados 
 Fahrenheit.
'''
# Incorporo función ya creada

from utilidades import controlar_repuesta_s_n


def presentacion():
    print('\t\n*********************************************************')
    print('\t\nPrograma que convierte grados Celsius a grados Fahrenheit')
    print('\t\n*********************************************************\n')


def gCelsius(celsius):
    Fahrenheit = (float(celsius) * 1.8) + 32
    print(f"El resultado es: {Fahrenheit} grados Fahrenheit")


def comienza():
    respuesta = 's'
    celsius = 0
    while respuesta == 's':
        try:
            celsius = int(input("Introduce los grado Celsius: "))
            gCelsius(celsius)
            respuesta = controlar_repuesta_s_n()

        except ValueError:
            print("El dato tiene que ser númerico, intentelo otra vez.")


presentacion()
comienza()
