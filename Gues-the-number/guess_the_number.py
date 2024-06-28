import random # Importa el modulo random para generar numeros aleatorios.


def adivina_el_numero(x):
    # Funcion que implementa el juego de adivinar el numero.

    print("===========================")
    print("  ¡Bienvenido/a al juego!  ")
    print("===========================")
    print(" Adivina el número secreto ")
    print("===========================")
    # Imprime mensajes de bienvenida e instrucciones para el usuario.

    numero_aleatorio = random.randint(1, x) # Genera un numero aleatorio entre 1 y x.

    prediccion = 0 # Inicializa la variable prediccion.

    while prediccion != numero_aleatorio:
        # Bucle que continua hasta que el usuario adivine el numero.

        # El usuario ingresa un numero.
        prediccion = int(input(f"Adivina un número entre 1 y {x}: ")) # Solicita al usuario que ingrese un numero, usando f-string para incluir el valor de x.
        # Con int convertimos a entero.

        if prediccion < numero_aleatorio:
            print("Intenta otra vez. Este número es más pequeño que el número secreto.")
            # Informa al usuario que el numero ingresado es menor que el numero secreto.
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. Este número es más grande que el número secreto.")
            # Informa al usuario que el numero ingresado es mayor que el número secreto.
    
    print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} correctamente.")


adivina_el_numero(10) # Llama a la funcion con el valor 10 como argumento.