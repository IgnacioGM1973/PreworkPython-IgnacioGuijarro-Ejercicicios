# Funciones globales

# Controla respuesta (s/n)
def controlar_repuesta_s_n():
    while True:
        respuesta = input("¿Desea continuar añadiendo valores? (s/n): ")
        if respuesta.lower() in ['s', 'n']:
            return respuesta.lower()
        else:
            print("Por favor, responda con 's' para sí o 'n' para no.")


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
