

def factorial(n):
    if n == 1:
        return n
    else:
        return factorial(n-1)*n


assert factorial(6) == 720

print(factorial(3))

