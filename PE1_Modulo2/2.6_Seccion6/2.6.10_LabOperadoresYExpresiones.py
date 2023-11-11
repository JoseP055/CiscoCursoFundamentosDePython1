# LAB

# Enunciado

# Tu tarea es completar el código para poder evaluar la siguiente expresión:
# ((x ** 2 + 1) / (x + 1)) - (2 * x / (x + 1))

# Resultado debe ser asignado a y.
# Se cauteloso, observa los operadores y priorízalos.
# Utiliza cuantos paréntesis sean necesarios.

# Puedes utilizar variables adicionales para acortar la expresión (sin embargo, no es muy necesario).
# Prueba tu código cuidadosamente.

# Datos de Prueba
# Entrada de muestra:
# 1
# Salida esperada:
# y = 0.6000000000000001

# Entrada de muestra:
# 10
# Salida esperada:
# y = 0.09901951266867294

# Entrada de muestra:
# 100
# Salida esperada:
# y = 0.009999000199950014

# Entrada de muestra:
# -5
# Salida Esperada:
# y = -0.19258202567760344

x = float(input("Ingresa un valor para X:\n"))

y = (1 / (x + (1 / (x + (1 / (x + (1 / x)))))))
# or
y = 1./(x + 1./(x + 1./(x + 1./x)))

print("Tu valor de y es: " + str(y))