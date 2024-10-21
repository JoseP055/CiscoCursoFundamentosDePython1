# Definamos una función que calcula el Índice de Masa Corporal (IMC).
# Valores peso (originalmente en kilogramos), altura (originalmente en metros)
# IMC = Altura / Metros ^2

def bmi(weight, height):
    return weight / height ** 2

print(bmi(52.5, 1.65))

#diagonal invertida (\) es empleado. Si se termina una línea de código con el, Python entenderá que la línea continua en la siguiente.

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))

def lb_to_kg(lb):
    return lb * 0.45359237

print(lb_to_kg(1))

def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254

print(ft_and_inch_to_m(1, 1))

print(ft_and_inch_to_m(6, 0))

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


print(ft_and_inch_to_m(6))

# ¿Cuál es el IMC de una persona que tiene 5'7" de altura y un peso de 176 lbs?
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.4535923


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2

print("Answer:")
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

