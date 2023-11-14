# LAB

# Enunciado

# Espatifilo, más comúnmente conocida como la planta de Cuna de Moisés o flor de la paz, es una de las plantas para interiores más populares que
# filtra las toxinas dañinas del aire. Algunas de las toxinas que neutraliza incluyen benceno, formaldehído y amoníaco.

# Imagina que tu programa de computadora ama estas plantas. Cada vez que recibe una entrada en forma de la palabra Espatifilo, grite
# involuntariamente a la consola la siguiente cadena: "¡Espatifilo es la mejor planta de todas!"

# Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:

# imprima el enunciado "Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!" en la pantalla
# si la cadena ingresada es "ESPATIFILIO" (mayúsculas)
# imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo" (minúsculas)
# imprima "¡Espatifilo!, ¡No [entrada]!" de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.
# Prueba tu código con los datos que te proporcionamos. ¡Y hazte de un Espatifilo también!

# Datos de Prueba:

# Entrada de muestra: espatifilo
# Salida esperada: No, ¡quiero un gran Espatifilo!

# Entrada de muestra: pelargonio
# Salida esperada: ¡Espatifilo!, ¡No pelargonio!

# Entrada de muestra: Espatifilo
# Salida esperada: Si, ¡El Espatifilo! es la mejor planta de todos los tiempos!

entrada = input("Ingresa un tipo de planta\n")
palabra_clave = "Espatifilo"
if entrada == palabra_clave:
    print("Si, ¡El Espatifilo! es la mejor planta de todos los tiempos!")
elif entrada == palabra_clave.lower():
    print("No, ¡quiero un gran Espatifilo!")
elif entrada == palabra_clave.upper():
    print("No, ¡quiero un pequeno Espatifilo!")
else:
    print(f"¡Espatifilo!, ¡No {entrada}!")