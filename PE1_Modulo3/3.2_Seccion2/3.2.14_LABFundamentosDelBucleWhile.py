# LAB

# Enunciado:

# Un niño y su padre, un programador de computadoras, construyen una pirámide con bloques de madera.

# Forma de la pirámide: La pirámide es plana y se construye de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.

# Regla de construcción: La altura de la pirámide se mide por el número de capas completas. Si no hay suficientes bloques para completar la
# siguiente capa, los constructores terminan su trabajo.

# Ilustración de la regla de construcción: Se proporciona una figura que muestra cómo se apilan los bloques para seguir la regla mencionada.

# Tarea del programa: Escribir un programa que lea la cantidad de bloques disponibles y genere la altura de la pirámide que se puede construir con esos bloques.

# Pruebas del programa:

# Prueba 1:

# Entrada: 6 bloques
# Salida esperada: La altura de la pirámide es: 3
# Prueba 2:

# Entrada: 20 bloques
# Salida esperada: La altura de la pirámide: 5
# Prueba 3:

# Entrada: 1000 bloques
# Salida esperada: La altura de la pirámide: 44
# Prueba 4:

# Entrada: 2 bloques
# Salida esperada: La altura de la pirámide: 1

#########################################################

# Solicita al usuario ingresar la cantidad de bloques
blocks = int(input("Ingresa el número de bloques: "))

# Inicializa las variables para la altura y la capa actual
height = 0
layer = 1

# Mientras haya bloques disponibles para construir una capa
while layer <= blocks:
    # Incrementa la altura de la pirámide
    height += 1
    # Reduce la cantidad de bloques utilizados en la capa actual
    blocks -= layer
    # Incrementa el número de la capa actual
    layer += 1

# Imprime la altura final de la pirámide
print("La altura de la pirámide:", height)

