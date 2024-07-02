import random # Importa el modulo random para generar numeros aleatorios.

def guess_the_number_pc(x):
    # Funcion que implementa el juego donde la computadora adivina el numero del usuario.

    print("=======================")
    print("¡Bienvenido/a al juego!")
    print("=======================")
    print(f"Piensa un número entre 1 y {x} para que la computadora intente adivinarlo.\n")
    # Imprime mensajes de bienvenida e instrucciones para el usuario.

    limite_inferior = 1 # Define el limite inferior del rango de busqueda.
    limite_superior = x # Define el limite superior del rango de busqueda.

    respuesta = "" # Inicializa la variable respuesta.
    while respuesta != "c":
        # Bucle que continua hasta que la computadora adivine el numero.

        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
            # Genera una prediccion aleatoria entre el limite inferior y el limite superior.
        else:
            prediccion = limite_inferior # Tambien podria ser el limite_superior. Si los limites inferior y superior son iguales, la predicción es ese valor.

        respuesta = input(f"Mi predicción es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C)\n").lower() 
        # Solicita al usuario que ingrese si la predicción es alta (A), baja (B) o correcta (C), y convierte la respuesta a minusculas.
        # Alt + z para reubicar las lineas.

        if respuesta == "a":
            limite_superior = prediccion - 1
             # Ajusta el limite superior si la prediccion es muy alta.
        elif respuesta == "b":
            limite_inferior = prediccion + 1
            # Ajusta el limite inferior si la prediccion es muy baja.

    print(f"La computadora adivinó tu número, {prediccion}")
    # Mensaje de felicitacion una vez que la computadora adivina el numero.


guess_the_number_pc(10)