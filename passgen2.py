# creador de contraseñas seguras segun la longitud requerida por el usuario

import string
import random

# creamos una funcion para generar contraseña
# dentro de esta funcion colocamos la longitud y los caracteres a incluir y a evitar
def generar_contrasena(longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiales=True, evitar_ambiguos=False):

    # Dependiendo de los parámetros, define qué grupos de caracteres incluir.
    #Si no se desea incluir un grupo, se asigna una cadena vacía ("").
    mayusculas = string.ascii_uppercase if incluir_mayusculas else ""
    minusculas = string.ascii_lowercase if incluir_minusculas else ""
    numeros = string.digits if incluir_numeros else ""
    especiales = string.punctuation if incluir_especiales else ""
    
    # Si evitar_ambiguos es True, elimina los caracteres ambiguos de cada grupo utilizando comprensión de listas.
    if evitar_ambiguos:
        ambiguos = "Il1O0"
        mayusculas = ''.join(c for c in mayusculas if c not in ambiguos)
        minusculas = ''.join(c for c in minusculas if c not in ambiguos)
        numeros = ''.join(c for c in numeros if c not in ambiguos)
        especiales = ''.join(c for c in especiales if c not in ambiguos)
    
    # Combina todos los caracteres seleccionados.
    # Si no se selecciona ningún grupo, lanza un error porque no se puede generar una contraseña.
    caracteres = mayusculas + minusculas + numeros + especiales
    if not caracteres:
        raise ValueError("Debe seleccionar al menos un tipo de caracteres.")
    
    # Usa random.choice para seleccionar caracteres aleatorios del conjunto caracteres.
    # Genera una lista de longitud elementos y luego los une en una cadena con "".join().
    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

    #Solicita una respuesta al usuario ('s' o 'n') y valida la entrada.
def solicitar_opcion(mensaje):

    while True:
        respuesta = input(mensaje).lower()
        if respuesta in ['s', 'n']:
            return respuesta == 's'  # Devuelve True si es 's', False si es 'n'
        else:
            print("Por favor, ingrese 's' para sí o 'n' para no.")


def main():
    print("Bienvenido al generador de contraseñas seguras.")
    try:
        # le pedimos la informacion al usuario tanto la longitud como los valores que se tomaran en cuenta para la generacion
        longitud = int(input("Ingrese la longitud de la contraseña: "))

        #Asegura que la longitud de la contraseña sea válida.
        if longitud < 1:
            print("La longitud debe ser mayor a 0.")
            return
        
        incluir_mayusculas = solicitar_opcion("¿Incluir mayúsculas? (s/n): ")
        incluir_minusculas = solicitar_opcion("¿Incluir minúsculas? (s/n): ")
        incluir_numeros = solicitar_opcion("¿Incluir números? (s/n): ")
        incluir_especiales = solicitar_opcion("¿Incluir caracteres especiales? (s/n): ")
        evitar_ambiguos = solicitar_opcion("¿Evitar caracteres ambiguos (0, O, 1, l, etc.)? (s/n): ")
        
        #llamamos la funcion y la mostramos
        contrasena = generar_contrasena(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_especiales, evitar_ambiguos)
        print(f"La contraseña generada es: {contrasena}")
        
        #Preguntamos al usuario si quiere guardar la contraseña
        # Usa with open() para abrir el archivo contrasenas.txt en modo de añadir ("a").
        # Escribe la contraseña en el archivo y lo cierra automáticamente.
        guardar = input("¿Desea guardar esta contraseña en un archivo? (s/n): ").lower()
        if guardar == 's':
            with open("contrasenas.txt", "a") as archivo:
                archivo.write(f"{contrasena}\n")
            print("Contraseña guardada exitosamente en 'contrasenas.txt'.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
