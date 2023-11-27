# LAB

# Enunciado
# En el problema, el mago junior guarda un número secreto en la variable "secret_number" y propone un juego llamado "Adivina el número secreto".
# Si los jugadores no adivinan el número, quedan atrapados en un bucle sin fin.
# La tarea del código consiste en solicitar al usuario que ingrese un número entero, utilizando un bucle while para repetir la interacción hasta
# que el usuario adivine el número secreto. Se verifica si el número ingresado coincide con el número secreto,
#  Si el número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje "¡Ja, ja! ¡Estás atrapado en
# mi bucle!" y se le solicitará que ingrese un número nuevamente. Si el número ingresado por el usuario coincide con el número escogido por el
# mago, el número debe imprimirse en la pantalla, y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora."
# Además, se destaca el uso de la función print() en una forma de impresión multilínea con comillas triples para mejorar la presentación del 
# texto.

secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

number = int(input("Ingresa un número entero: "))
while number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    number = int(input("Ingresa un número entero: "))

print("¡Bien hecho, muggle! Eres libre ahora.")
