

import importlib
from utilidades import menu

# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def main():
    print(Fore.BLUE + '\n' + '-' * 70)
    nombre = input("Hola, Introduce tu nombre por favor: ")
    print(Fore.LIGHTBLUE_EX + f"Encantado, {nombre.title()}")
    print('-' * 70 + Style.RESET_ALL + "\n")

    while True:

        print(Fore.YELLOW + f"¿Qué ejercicio deseas visualizar?" +
              Style.RESET_ALL + "\n")

        menu()
        respuesta = input(
            "Introduce un número del 1 al 20 (o 'salir' para terminar): ")
        if respuesta.lower() == 'salir':
            print(Fore.CYAN + '\n' + '*' * 70)
            print('                              Hasta otra!!')
            print('*' * 70 + Style.RESET_ALL + "\n")
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
        # Espera a que el usuario pulse Enter para continuar. Así puedo ver el resultado antes que salga otra vez el menu.
        input("\nPulsa Enter para continuar...")


if __name__ == "__main__":
    main()
