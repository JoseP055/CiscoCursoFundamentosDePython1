# Aquí se presentan algunos programas simples que utilizan listas:

# Encontrar el Valor Máximo:

# Se asume que el primer elemento de la lista es el más grande.
# Se compara esta hipótesis con todos los elementos restantes de la lista.
# El código muestra el valor más grande en la lista (17 en este caso).

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)

# Ubicación de un Elemento Dado:

# Busca la ubicación de un elemento específico en una lista.
# Utiliza un bucle for y la variable found para controlar el estado de la búsqueda.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemento encontrado en el índice", i)
else:
    print("Ausente")

# Contar Aciertos en la Lotería:

# Determina cuántos números acertaste en una lotería.
# Utiliza un bucle for para comparar los números jugados con los números sorteados.
# La salida es la cantidad de aciertos (4 en este caso).

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)