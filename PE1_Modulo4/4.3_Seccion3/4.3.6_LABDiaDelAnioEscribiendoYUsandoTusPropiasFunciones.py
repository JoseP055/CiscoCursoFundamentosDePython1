# LAB

# Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y 
# devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.

def bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def dias_mes(year,month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and bisiesto(year):
        res = 29
    return res

def dia_anio(year, month, month_day):
    if year < 1582 or month < 1 or month > 12 or month_day < 1 or month_day > 31:
        return None
    year_day = 0
    for m in range(1, month):
        md = dias_mes(year, m)
        if md == None:
            return None
        year_day += md
    md = dias_mes(year, month)
    if month_day >= 1 and month_day <= md:
        return year_day + month_day
    else:
        return None 
    
print(dia_anio(2000,2,29))