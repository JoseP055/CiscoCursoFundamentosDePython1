# LAB

# Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el 
# número de días del mes/año dado (mientras que solo febrero es sensible al valor year, tu función 
# debería ser universal).

def bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def diasMes(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]
    if month in days_31:
        return 31
    if month in days_30:
        return 30
    if month == 2:
        if bisiesto(year) == True:
            return 29
        else:
            return 28
        
# Otra forma
def days_in_month(year,month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and bisiesto(year):
        res = 29
    return res

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = diasMes(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
