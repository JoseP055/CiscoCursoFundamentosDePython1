def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# Ejemplo de argumentos posicionales
adding(1, 2, 3)  # Salida: 1 + 2 + 3 = 6

# Ejemplo de argumentos con palabras clave
adding(c=1, a=2, b=3)  # Salida: 2 + 3 + 1 = 6

# Ejemplo de combinación de argumentos posicionales y con palabras clave
adding(3, c=1, b=2)  # Salida: 3 + 2 + 1 = 6

# Ejemplo de error al intentar pasar múltiples valores a un argumento
# Esto provocará un error: TypeError: adding() got multiple values for argument 'a'
# adding(3, a=1, b=2)