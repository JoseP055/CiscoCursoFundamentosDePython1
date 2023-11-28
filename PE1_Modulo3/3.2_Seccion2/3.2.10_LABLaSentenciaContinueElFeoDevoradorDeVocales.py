# LAB

# ENUNCIADO

# La sentencia continue se usa para omitir el bloque actual y avanzar a la siguiente iteración, sin ejecutar las sentencias dentro del bucle.

# Se puede usar tanto con bucles while y for.

# Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! Escribe un programa que use:

# un bucle for;
# el concepto de ejecución condicional (if-elif-else).
# la sentencia continue.
# Tu programa debe:

# pedir al usuario que ingrese una palabra.
# utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el método upper() muy pronto, no te preocupes
# utiliza la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A, E, I, O, U de la palabra ingresada.
# imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada
# Prueba tu programa con los datos que le proporcionamos.


# Datos de Prueba:
# Entrada de muestra:

# Gregory
# Salida esperada:

# G
# R
# G
# R
# Y

# Entrada de muestra:

# abstemious
# Salida esperada:

# B
# S
# T
# M
# S

# Entrada de muestra:

# IOUEA
# Salida esperada:

user_word = input("Ingresa una palabra, para devorar sus vocales:\n")
user_word = user_word.upper()

for lettter in user_word:
    if lettter == "A":
        continue
    elif lettter == "E":
        continue
    elif lettter == "I":
        continue
    elif lettter == "O":
        continue
    elif lettter == "U":
        continue
    else:
        print(lettter)