# LAB

# Tu tarea es escribir una función que verifique si un número es primo o no.

def is_prime(value):
    if value < 2:
        return False
    else:
        for i in range(2, int(value ** 0.5) + 1):
            if value % i == 0:
                return False
        return True
    
for i in range(2, 20):
    if is_prime(i):
        print(i , end=" ")
print()