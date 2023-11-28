# LAB

# Enunciado:

# En 1937, el matemático alemán Lothar Collatz formuló una hipótesis intrigante sobre secuencias de números.
# La hipótesis sugiere que, partiendo de cualquier número entero positivo distinto de cero, aplicando ciertas reglas, eventualmente se llega al número 1.

# Reglas de la hipótesis de Collatz:

# Tome un número entero no negativo y no cero, llámelo c0.
# Si c0 es par, evalúe un nuevo c0 como c0 ÷ 2.
# Si c0 es impar, evalúe un nuevo c0 como 3 × c0 + 1.
# Repita los pasos 2 y 3 hasta que c0 sea igual a 1.
# Objetivo del programa: Escribir un programa en Python que lea un número natural y aplique las reglas de la hipótesis de Collatz hasta que c0
# sea igual a 1. El programa debe contar los pasos necesarios y mostrar todos los valores intermedios de c0.

# Ejemplos de prueba:

# Entrada: 15

# Salida esperada:
# 46
# 23
# ...
# 1
# pasos = 17
# Entrada: 16

# Salida esperada:
# makefile

# 8
# 4
# 2
# 1
# pasos = 4
# Entrada: 1023

# Salida esperada:

# 3070
# 1535
# ...
# 2
# 1
# pasos = 62
# Sugerencia: La implementación debe utilizar un bucle while para aplicar las reglas de Collatz y contar los pasos hasta llegar a 1.

c0 = int(input("Ingresa un número entero positivo: "))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 /= 2
    else:
        c0 = 3 * c0 + 1
    print(int(c0))
    steps += 1

print("Pasos =", steps)