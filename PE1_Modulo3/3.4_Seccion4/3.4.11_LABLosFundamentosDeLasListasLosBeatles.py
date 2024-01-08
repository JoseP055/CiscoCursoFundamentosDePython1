# LAB
# ENUNCIADO

# Tu tarea es:

# paso 1: crea una lista vacía llamada beatles;
# paso 2: emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison;
# paso 3: emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best;
# paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista;
# paso 5: usa el método insert() para agregar a Ringo Starr al principio de la lista.

# Paso #1
beatles = []
print("Lista de Integrantes de los Beatles:", beatles)

# Paso #2
first_members = ["John Lennon","Paul McCartney", "George Harrison"]
for i in first_members:
    beatles.append(i)
print("Lista de Integrantes de los Beatles:", beatles)

# Paso #3
left_members = ["Stu Sutcliffe", "Pete Best"]
while left_members != []:
    for i in left_members:
        user_select = input(f"Agregue a los miembros restantes para continuar, los miembros restantes son: {left_members}\n")
        try:
            if user_select == left_members[0]:
                beatles.append(left_members[0])
                del left_members[0]
            elif user_select == left_members[1]:
                beatles.append(left_members[1])
                del left_members[1]
            else:
                print("Integrante no encontrado")
        except IndexError as e:
            print("Integrante ya agregado")

print("Lista de Integrantes de los Beatles:", beatles)

# Paso #4
del beatles[-2]
del beatles[-1]
print("Lista de Integrantes de los Beatles:", beatles)

# Paso #5
beatles.insert(0, "Ringo Starr")
print("Lista de Integrantes de los Beatles:", beatles)