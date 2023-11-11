# LAB

# Enunciado
# La tarea consiste en preparar un código simple para evaluar o encontrar el tiempo final de un periodo dado, expresándolo en horas y minutos.
# La hora de inicio se da como un par de horas (0..23) y minutos (0..59). El resultado debe ser mostrado en la consola.

# Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.

# No te preocupes si tu código no es perfecto - está bien si acepta una hora inválida - lo más importante es que el código produzca una salida correcta acorde a la entrada dada.

# Prueba el código cuidadosamente. Pista: utilizar el operador % puede ser clave para el éxito.

# Datos de Prueba

# Entrada de muestra:
# 12
# 17
# 59

# Salida Esperada:
# 13:16

# Entrada de muestra:
# 23
# 58
# 642

# Salida Esperada:
# 10:40

# Entrada de muestra
# 0
# 1
# 2939

# Salida Esperada:
# 1:0

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aquí

total_min = (hour * 60 + mins + dura) # Se calcula el tiempo total de minutos

hora_final = (total_min // 60) % 24 # Total de minutos se divide a hora exacta y se pasa a formato de 24h
min_final = total_min % 60 # el total de min se le saca el resto de 60
print("EL evento finaliza a las: ",hora_final,":",min_final)
