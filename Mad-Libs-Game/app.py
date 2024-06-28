# Concatenar cadenas de caracteres.

organizacion = "42"

# Diferentes formas de concatenar cadenas de caracteres
print("Aprende a programar con " + organizacion) # Concatenación usando el operador +.
print("Aprende a programar con {}".format(organizacion)) # Concatenación usando el método format().
print(f"Aprende a programar con {organizacion}") # Concatenación usando una f-string.

# Mad Libs (Historias Locas)

"""
La función get_valid_input(prompt) se utiliza para obtener una entrada válida del usuario.
El bucle while se asegura de que la entrada no esté vacía y no contenga números.
Si la entrada es inválida, se muestra un mensaje de error y se solicita la entrada de nuevo.

def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if not user_input.strip():  # Verifica si la entrada está vacía o solo tiene espacios
            print("Error: La respuesta no puede estar en blanco. Por favor, inténtalo de nuevo.")
        elif any(char.isdigit() for char in user_input):  # Verifica si la entrada contiene algún número
            print("Error: La respuesta no puede contener números. Por favor, inténtalo de nuevo.")
        else:
            return user_input
"""

# Solicita al usuario diferentes tipos de palabras para completar las historias
adj = input("Escribe un adjetivo femenino singular: ")
verbo1 = input("Escribe un verbo infinitivo: ")
verbo2 = input("Escribe otro verbo infinitivo: ")
sustantivo_plural = input("Escribe un sustantivo (plural masculino): ")

# Definimos dos historias diferentes usando las palabras proporcionadas por el usuario
madlib1 = f"La travesía por la montaña fue absolutamente {adj}. Disfruté cada momento al {verbo1} por los senderos. A la noche, nos reunimos para {verbo2} alrededor del fuego. Nunca olvidaré esos {sustantivo_plural} mágicos." #Alt+Z para dividir la línea visualmente.

# Imprime las historias completas
madlib2 = f"La clase de cocina fue muy {adj}. Me gustó mucho {verbo1} recetas nuevas y luego {verbo2} los platos con mis compañeros. Al final, todos compartimos nuestros {sustantivo_plural} deliciosos."


print(madlib1)
print(madlib2)
