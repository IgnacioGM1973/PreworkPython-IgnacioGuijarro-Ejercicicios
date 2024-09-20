

import importlib


def main():
    nombre = input("Hola, Introduce tu nombre por favor: ")
    print(f"Encantado {nombre}")

    while True:
        print(f"¿Qué ejercicio deseas visualizar?. ")
        respuesta = input(
            "Introduce un número del 1 al 20 (o 'salir' para terminar): ")
        if respuesta.lower() == 'salir':
            print('Hasta luego!!')
            break
        if respuesta.isdigit() and 1 <= int(respuesta) <= 20:
            try:
                # Importación dinámica del módulo de ejercicios
                modulo = importlib.import_module(f"ejercicio{respuesta}")
                # Asume que cada módulo tiene una función 'run' para ejecutar el ejercicio.
                modulo.run()
            except ModuleNotFoundError:
                print(f"El ejercicio {respuesta} no está disponible.")
            except AttributeError:
                print(f"El ejercicio {respuesta} no tiene una función 'run'.")
        else:
            print("Por favor, introduce un número válido entre 1 y 20.")


if __name__ == "__main__":
    main()
