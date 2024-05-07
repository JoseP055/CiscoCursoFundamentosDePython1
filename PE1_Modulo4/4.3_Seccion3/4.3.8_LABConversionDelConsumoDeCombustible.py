# LAB

#Tu tarea es escribir un par de funciones que conviertan l/100km a mpg (milas por galón), y viceversa.

#Las funciones:

# llaman liters_100km_to_miles_gallon y miles_gallon_to_liters_100km respectivamente;
# toman un argumento (el valor correspondiente a sus nombres)

def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    litters =  3.785411784 
    km = miles * 1609.344 / 1000 / 100
    return litters / km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
