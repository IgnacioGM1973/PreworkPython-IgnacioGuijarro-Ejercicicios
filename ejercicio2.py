'''
 Ejercicio 2: Calculadora de Propina
 Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
 una propina del 15% sobre el total de la cuenta
'''

# Incorporo función ya creada

from utilidades import controlar_repuesta_s_n

# Para agregar color en terminales que lo soporten
try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = lambda x: x  # Si no se puede importar, no aplicar color


def presentacion():
    print(Fore.CYAN + '\n' + '*' * 70)
    print(' ' * 10 + 'Bienvenido a la Calculadora de Propina'.center(50))
    print('*' * 70 + Style.RESET_ALL)
    print('\nEste programa calcula el monto total a pagar en un restaurante,')
    print('incluyendo una propina del 15% sobre el total de la cuenta.\n')


def cCuenta():
    lista = []
    respuesta = 's'
    conta = 1

    while respuesta == 's':
        try:
            pedido = float(input(f"\n{Fore.YELLOW}Introduzca el valor del pedido número {
                           conta}: €{Style.RESET_ALL}"))
            lista.append(pedido)
            conta += 1
            respuesta = controlar_repuesta_s_n()

        except ValueError:
            print(
                Fore.RED + "Valor incorrecto. Por favor, introduzca un número válido." + Style.RESET_ALL)

    totalLista = sum(lista)
    propina = 0.15 * totalLista
    cantidadPagar = totalLista + propina
    promedioPedido = totalLista / len(lista) if lista else 0

    print(Fore.GREEN + '\n' + '-' * 70)
    print(f'La cantidad total sin aplicar la propina es: {totalLista:.2f}€')
    print(f'La propina es de: {propina:.2f}€ (Aplicando el 15%)')
    print(f"La cantidad total aplicando la propina es: {cantidadPagar:.2f}€")
    print(f"Número de pedidos: {len(lista)}")
    print(f"Promedio por pedido: {promedioPedido:.2f}€")
    print('-' * 70 + Style.RESET_ALL)


# Ejecución del programa
presentacion()
cCuenta()
