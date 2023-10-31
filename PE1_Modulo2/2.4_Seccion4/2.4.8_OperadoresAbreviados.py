# Si se necesita calcular una serie de valores sucesivos de la potencia de 2, se puede usar el siguiente código:
x = 2
sheep = 0
x = x * 2
print(x)

# Otro ejemplo para sumar de 1 en 1
sheep = sheep + 1
print(sheep)

# Una forma simple de hacerlo es con 
x *= 2 
sheep += 1

# Esto gracias a lo siguiente:
# (variable = variable op expresión) = (variable op= expresión)

# Expresión	               | Operador abreviado
#
#  i = i + 2 * j           |     i += 2 * j
# var = var / 2            |      var /= 2
# rem = rem % 10           |      rem %= 10
# j = j - (i + var + rem)  |  j -= (i + var + rem)
# x = x ** 2               |      x **= 2