# LAB

# Crea una lista de números enteros con algunas repeticiones.
# Desarrolla un programa en Python que elimine las repeticiones de la lista.
# Utiliza una lista temporal para almacenar los elementos únicos.
# Itera sobre la lista original y agrega cada número a la lista temporal si no está presente.
# Imprime la lista original y la lista resultante sin repeticiones.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

my_list_2 = []

for elem in my_list:
    if elem not in my_list_2:
        my_list_2.append(elem)


print("La lista con elementos originales:")
print(my_list)
print("La lista con elementos únicos:")
print(my_list_2)
