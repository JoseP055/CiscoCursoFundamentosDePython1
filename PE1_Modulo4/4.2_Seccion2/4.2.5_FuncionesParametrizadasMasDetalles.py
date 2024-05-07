# En ocasiones ocurre que algunos valores de ciertos argumentos son más utilizados que otros. Dichos 
# argumentos tienen valores predefinidos los cuales pueden ser considerados cuando los argumentos 
# correspondientes han sido omitidos.

def introduction(first_name, last_name="Smith"):
    print("Hola, mi nombre es", first_name, last_name)


introduction("Jorge", "Pérez")
# Resultado = Hola, mi nombre es Jorge Pérez

introduction("Enrique")
# Resultado = Hola, mi nombre es Enrique Smith

introduction(first_name="Guillermo")
# Resultado = Hola, mi nombre es Guillermo Smith

# Se puede hacer con más parámetros, si te resulta útil. Ambos parámetros tendrán sus valores por 
# defecto, observa el siguiente código:

def introduction(first_name="Juan", last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)

introduction()
# Resultado = Hola, mi nombre es Juan González