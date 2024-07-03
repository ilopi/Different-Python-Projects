import random # Importa el modulo random para generar elecciones aleatorias para la computadora.


def jugar():
    # Solicita al usuario que ingrese su eleccion y la convierte a minusculas.
    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijeras.\n").lower()
    # La computadora elige aleatoriamente entre 'pi', 'pa' y 'ti'.
    computadora = random.choice(['pi', 'pa', 'ti'])

     # Compara las elecciones del usuario y de la computadora para determinar si es un empate.
    if usuario == computadora:
        return '¡Empate!'
    
    # Llama a la funcion gana_jugador para determinar si el usuario gana.
    if gana_jugador(usuario, computadora):
        return '¡Ganaste!'
    
    # Si no es un empate y el usuario no gana, entonces la computadora gana.
    return '¡Perdiste!'


def gana_jugador(jugador, oponente):
    # Retornar True si gana el jugador.
    # Piedra gana a Tijera. pi > ti.
    # Tijera gana a Papel. ti > pa.
    # Papel gana a Piedra. pa > pi.
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False
    

# Llama a la funcion jugar e imprime el resultado.
print(jugar())