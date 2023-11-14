# LAB

# Enunciado

# Usando uno de los operadores de comparación en Python, escribe un programa simple de dos líneas que tome el parámetro n
# como entrada, que es un entero, e imprime False si n es menor que 100, y True if n es mayor o igual que 100.
# No debes crear ningún bloque if (hablaremos de ellos muy pronto). Prueba tu código usando los datos que te proporcionamos.

# Datos a usar
#Entrada de muestra: 55
# Salida esperada: False

# Entrada de muestra: 99
# Salida esperada: False

# Entrada de muestra: 100
# Salida esperada: True

# Entrada de muestra: 101
# Salida esperada: True

# Entrada de muestra: -5
# Salida esperada: False

# Entrada de muestra: +123
# Salida esperada: True

n = int(input("Ingrese un valor numerico entero\n"))
answer = n >= 100

print(f"Tu numero {n}, es mayor o igual a 100? :  {answer}")