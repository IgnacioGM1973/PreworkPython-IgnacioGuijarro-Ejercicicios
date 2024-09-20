# Funciones globales

# Controla respuesta (s/n)
def controlar_repuesta_s_n():
    while True:
        respuesta = input("¿Desea continuar añadiendo valores? (s/n): ")
        if respuesta.lower() in ['s', 'n']:
            return respuesta.lower()
        else:
            print("Por favor, responda con 's' para sí o 'n' para no.")


# Bloque de código que solo se ejecutará si el archivo es ejecutado directamente
if __name__ == "__main__":
    print("")
