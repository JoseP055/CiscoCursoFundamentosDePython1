# Recursividad

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

for n in range(1, 11):
    print(n, "->", fib(n))

for n in range(1, 11):
    print(n, "->", factorial_function(n))