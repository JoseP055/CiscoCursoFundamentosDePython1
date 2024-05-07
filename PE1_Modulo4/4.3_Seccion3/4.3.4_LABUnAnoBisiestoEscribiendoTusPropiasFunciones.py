# LAB

#Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es 
# un año bisiesto, o False si no lo es. Luego corroborar en un lista de años si los resultados son
# correctos o fallan.

def bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = bisiesto(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")