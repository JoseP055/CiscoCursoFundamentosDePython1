# LAB

# ENUNCIADO

# La instrucción break se implementa para salir/terminar un bucle.

# Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese una palabra a menos que ingrese "chupacabra" como la
# palabra de output secreta, en cuyo caso el mensaje "Has dejado el bucle con éxito." debe imprimirse en la pantalla y el bucle debe terminar.

# No imprimas ninguna de las palabras ingresadas por el usuario. Utiliza el concepto de ejecución condicional y la sentencia break.
palabra = ""
while (True):
    palabra = input("Ingresa una palabra\n")
    if palabra == "chupacabra":
        break

print("Has dejado el bucle con éxito.")