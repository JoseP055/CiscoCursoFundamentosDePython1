#LAB
#Escenario
# Millas y kilómetros son unidades de longitud o distancia.

# Teniendo en mente que 1 milla equivale aproximadamente a 1.61 kilómetros, complementa el programa en el editor para que convierta de:

# Millas a kilómetros;
# Kilómetros a millas.
# Nota: No se debe alterar el codigo fuente solo los espacios donde estan los ###
# Salida Esperada
# 7.38 millas son 11.88 kilómetros
# 12.25 kilómetros son 7.61 millas


kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

# la funcion round() se usa para redondear a uan cantidad especifica de decimales. En ese case se redondean a 2 decimales

