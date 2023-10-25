# LAB
# Enunciado

# con base a esto 
#print("    *")
#print("   * *")
#print("  *   *")
#print(" *     *")
#print("***   ***")
#print("  *   *")
#print("  *   *")
#print("  *****")

#Intenta:

#1 minimizar el número de invocaciones de la función print() insertando \n en las cadenas;
#2 hacer que la flecha sea el doble de grande (pero mantener las proporciones)
#3 duplica la flecha, colocando ambas flechas una al lado de la otra; nota: una cadena se puede multiplicar usando el siguiente truco: "string" * 2 producirá "stringstring" (pronto contaremos más al respecto)
#4 elimina cualquiera de las comillas y observe detenidamente la respuesta de Python; presta atención a dónde Python ve un error - ¿es este el lugar donde realmente existe el error?
#5 haz lo mismo con algunos de los paréntesis;
#6 cambia cualquiera de las palabras print por otra cosa, que difiera solo en mayúsculas y minúsculas (por ejemplo, Print) - qué sucede ahora?
#7 reemplaza algunas de las comillas con apóstrofes; observa lo que sucede con cuidado.

############################################################################################

#1
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")  # Logrado

#2
print("        *\n       * *\n      *   *\n     *     *\n    *       *\n   *         *\n  *           *\n *             *\n*****       *****\n    *       *\n    *       *\n    *       *\n    *       *\n    *********") # Logrado

#3
print("     *     " * 2)
print("    * *    " * 2)
print("   *   *   " * 2)
print("  *     *  " * 2)
print(" ***   *** " * 2)
print("   *   *   " * 2)
print("   *   *   " * 2)
print("   *****   " * 2)
# Logrado

#4 
# print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****) inidica que las comillas nunca fueron cerradas

#5
# print"    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****"") inidica que las parentesis nunca fueron abiertos

#6
#Print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****") Da name error porque reconoce a Print como una funcion del usuario y no de Python y dicha funcion no esta definida
#7
print('    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****') # No pasa nada
